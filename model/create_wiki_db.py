# SOURCE


import sqlite3
import csv


# Set up the database connection
conn = sqlite3.connect("../data/wiki_people.db")

wiki_people_DATA_PATH = "/Users/wadewilson/sbox/PycharmProjects/realestate_data/data/"

# TODO reformat this to put path in main function
# TODO reformat this to move path and db info in .env
sqlite_file = rf"{wiki_people_DATA_PATH}wiki_people.db"
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


# Create a table to store the people data
sqlite_create = """CREATE TABLE IF NOT EXISTS people
             (wikidata_code TEXT,
             birth INTEGER,
             death INTEGER,
             updated_death_date TEXT,
             approx_birth INTEGER,
             approx_death INTEGER,
             birth_min INTEGER,
             birth_max INTEGER,
             death_min INTEGER,
             death_max INTEGER,
             gender TEXT,
             level1_main_occ TEXT,
             name TEXT,
             un_subregion TEXT,
             birth_estimation TEXT,
             death_estimation TEXT,
             bigperiod_birth_graph_b TEXT,
             bigperiod_death_graph_b TEXT,
             curid TEXT,
             level2_main_occ TEXT,
             freq_main_occ REAL,
             freq_second_occ REAL,
             level2_second_occ TEXT,
             level3_main_occ TEXT,
             bigperiod_birth TEXT,
             bigperiod_death TEXT,
             wiki_readers_2015_2018 INTEGER,
             non_missing_score REAL,
             total_count_words_b INTEGER,
             number_wiki_editions INTEGER,
             total_noccur_links_b INTEGER,
             sum_visib_ln_5criteria REAL,
             ranking_visib_5criteria INTEGER,
             all_geography_groups TEXT,
             string_citizenship_raw_d TEXT,
             citizenship_1_b TEXT,
             citizenship_2_b TEXT,
             list_areas_of_rattach TEXT,
             area1_of_rattachment TEXT,
             area2_of_rattachment TEXT,
             list_wikipedia_editions TEXT,
             un_region TEXT,
             group_wikipedia_editions TEXT,
             bplo1 REAL,
             dplo1 REAL,
             bpla1 REAL,
             dpla1 REAL,
             pantheon_1 REAL,
             level3_all_occ TEXT)"""

cursor.execute(sqlite_create)


# Open the CSV file and insert each row into the people table
with open(
    f"{wiki_people_DATA_PATH}cross-verified-database-2.csv",
    newline="",
    encoding="latin-1",
) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # TODO iteratively create the ? vs hard coding n # ?,
        cursor.execute(
            """INSERT INTO people VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["wikidata_code"],
                row["birth"],
                row["death"],
                row["updated_death_date"],
                row["approx_birth"],
                row["approx_death"],
                row["birth_min"],
                row["birth_max"],
                row["death_min"],
                row["death_max"],
                row["gender"],
                row["level1_main_occ"],
                row["name"],
                row["un_subregion"],
                row["birth_estimation"],
                row["death_estimation"],
                row["bigperiod_birth_graph_b"],
                row["bigperiod_death_graph_b"],
                row["curid"],
                row["level2_main_occ"],
                row["freq_main_occ"],
                row["freq_second_occ"],
                row["level2_second_occ"],
                row["level3_main_occ"],
                row["bigperiod_birth"],
                row["bigperiod_death"],
                row["wiki_readers_2015_2018"],
                row["non_missing_score"],
                row["total_count_words_b"],
                row["number_wiki_editions"],
                row["total_noccur_links_b"],
                row["sum_visib_ln_5criteria"],
                row["ranking_visib_5criteria"],
                row["all_geography_groups"],
                row["string_citizenship_raw_d"],
                row["citizenship_1_b"],
                row["citizenship_2_b"],
                row["list_areas_of_rattach"],
                row["area1_of_rattachment"],
                row["area2_of_rattachment"],
                row["list_wikipedia_editions"],
                row["un_region"],
                row["group_wikipedia_editions"],
                row["bplo1"],
                row["dplo1"],
                row["bpla1"],
                row["dpla1"],
                row["pantheon_1"],
                row["level3_all_occ"],
            ),
        )


conn.commit()
cursor.close()
