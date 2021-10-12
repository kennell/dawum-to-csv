#!/usr/bin/env python3
import csv
import io
import requests
from slugify import slugify


DAWUM_API_URL = 'https://api.dawum.de/'
SLUGIFY_GERMAN_UMLAUTS = [
    ['ä', 'ae'],
    ['Ä', 'Ae'],
    ['ö', 'oe'],
    ['Ö', 'Oe'],
    ['ü', 'ue'],
    ['Ü', 'Ue'],
]

rsp = requests.get(DAWUM_API_URL)
data = rsp.json()

# Parse Parliaments
parliaments = {}
for key, value in data['Parliaments'].items():
    parliaments[key] = {
        'parliament_id': slugify(value['Shortcut'], replacements=SLUGIFY_GERMAN_UMLAUTS),
        'parliament_name': value['Name']
    }

# Parse Institutes
institutes = {}
for key, value in data['Institutes'].items():
    institutes[key] = {
        'institute_id': slugify(value['Name'], replacements=SLUGIFY_GERMAN_UMLAUTS),
        'institute_name': value['Name'],
    }

# Parse Taskers
taskers = {}
for key, value in data['Taskers'].items():
    taskers[key] = {
        'tasker_id': slugify(value['Name'], replacements=SLUGIFY_GERMAN_UMLAUTS),
        'tasker_name': value['Name'],
    }

# Parse Parties
parties = {}
for key, value in data['Parties'].items():
    parties[key] = {
        'party_id': slugify(value['Shortcut'], replacements=SLUGIFY_GERMAN_UMLAUTS),
        'party_name': value['Name'],
    }

# Parse Surveys
surveys = {}
result_fieldnames = set()
for key, value in data['Surveys'].items():
    surveys[key] = {
        'survey_id': key,
        'survey_date': value['Date'],
        'survey_persons': value['Surveyed_Persons'],
        'survey_start': value['Survey_Period']['Date_Start'],
        'survey_end': value['Survey_Period']['Date_End'],
    }
    surveys[key].update(
        parliaments[value['Parliament_ID']]
    )
    surveys[key].update(
        taskers[value['Tasker_ID']]
    )
    surveys[key].update(
        institutes[value['Institute_ID']]
    )
    for party_id, result in value['Results'].items():
        col = 'result_' + parties[party_id]['party_id']
        result_fieldnames.add(col)
        surveys[key][col] = float(result)


f = io.StringIO()
fieldnames = [
    'survey_id', 'survey_date', 'survey_persons', 'survey_start', 'survey_end',
    'parliament_id', 'parliament_name',
    'institute_id', 'institute_name',
    'tasker_id', 'tasker_name',
]
fieldnames += result_fieldnames
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
for survey in surveys.values():
    writer.writerow(survey)
print(f.getvalue())