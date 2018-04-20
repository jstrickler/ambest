#!/usr/bin/python

from datetime import date

NUM_TERMS = 45

def mkdate(raw_date):
    if raw_date == "NONE":
        d = None
    else:
        raw_year, raw_month, raw_day = raw_date.split('-')
        d = date(int(raw_year), int(raw_month), int(raw_day))

    return d


def get_info(index):
    pres_data = {}
    with open("../DATA/presidents.txt") as pres_in:
        for line in pres_in:
            flds = line[:-1].split(":")
            if int(flds[0]) == index:
                pres_data["lastname"] = flds[1]
                pres_data["firstname"] = flds[2]

                pres_data["birthdate"] = mkdate(flds[3])
                pres_data["deathdate"] = mkdate(flds[4])

                pres_data["birthplace"] = flds[5]
                pres_data["birthstate"] = flds[6]

                pres_data["termstart"] = mkdate(flds[7])
                pres_data["termend"] = mkdate(flds[8])

                pres_data["party"] = flds[9]

                break

    return pres_data


def get_all_data():
    all_data = []
    for i in range(1, NUM_TERMS):
        all_data.append(get_info(i))
    return all_data


def get_age_at_term_end(pinfo):
    birthdate = pinfo["birthdate"]
    termend = pinfo["termend"]
    if termend is None:
        termend = date.today()
    age_at_end = termend - birthdate
    return age_at_end.days / 365.25


def get_age_extreme(*, get_youngest=True):
    all_raw = get_all_data()
    all_cooked = sorted(all_raw, key=get_age_at_term_end)
    return all_cooked[0] if get_youngest else all_cooked[-1]


def get_oldest():
    return get_age_extreme(get_youngest=False)


def get_youngest():
    return get_age_extreme()
