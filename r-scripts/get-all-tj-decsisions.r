library(httr)
library(jsonlite)
library(progress)
library(optparse)

paginate_through_judilibre_results <- function(key, url, params, endpoint = "export") {
  next_batch <- TRUE
  batch <- 0
  results <- list()

  while (next_batch) {
    params$batch <- batch

    response <- GET(
      url = paste0(url, "/", endpoint),
      query = params,
      add_headers(KeyId = key)
    )

    if (http_error(response)) {
      stop("Erreur dans la requête : ", status_code(response))
    }

    response_data <- content(response, as = "parsed", encoding = "UTF-8")

    if (!"results" %in% names(response_data)) {
      warning("Réponse inattendue à la batch ", batch)
      break
    }

    results <- append(results, response_data$results)

    if (is.null(response_data$next_batch)) {
      next_batch <- FALSE
    }

    batch <- batch + 1
  }

  return(results)
}

# === MAIN ===

option_list <- list(
  make_option(c("-k", "--key-id"), type = "character", help = "Clé API Judilibre"),
  make_option(c("-u", "--url"), type = "character", default = "https://api.piste.gouv.fr/cassation/judilibre/v1.0", help = "URL API"),
  make_option(c("-o", "--output-folder"), type = "character", default = "./data", help = "Dossier de sortie")
)

opt_parser <- OptionParser(option_list = option_list)
opt <- parse_args(opt_parser)

key_id <- opt$`key-id`
url <- opt$url
output_folder <- opt$`output-folder`

if (!dir.exists(output_folder)) {
  dir.create(output_folder, recursive = TRUE)
}

release_date <- as.Date("2023-12-15")
n_days <- as.integer(Sys.Date() - release_date)
dates <- sort(seq(release_date, by = "day", length.out = n_days))

pb <- progress_bar$new(
  format = "[:bar] :current/:total :start_date -> :end_date (:counter décisions)",
  total = length(dates) - 1,
  clear = FALSE,
  width = 80
)

params <- list(
  jurisdiction = "tj",
  batch_size = 1000
)
counter <- 0

for (i in 1:(length(dates) - 1)) {
  start_date <- dates[i]
  end_date <- dates[i + 1]

  params$date_start <- as.character(start_date)
  params$date_end <- as.character(end_date)

  pb$tick(tokens = list(start_date = start_date, end_date = end_date, counter = counter))

  results <- paginate_through_judilibre_results(key = key_id, url = url, params = params)

  for (r in results) {
    file_name <- file.path(output_folder, paste0("decision_", r$id, ".json"))
    write(toJSON(r, auto_unbox = TRUE, pretty = TRUE), file = file_name)
    counter <- counter + 1
  }
}
