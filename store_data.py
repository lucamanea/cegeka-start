import pickle

stored_data = {
    "personal": {
        "name": "Luca Manea",
        "birth date": "06/06/1998",
        "nationality": "Romanian",
        "gender": "Male",
        "address": "Cluj-Napoca",
        "mail": "manealuca@yahoo.com",
    },
    "experience": {
        "Python Software Developer": {
            "company": "Luxoft",
            "type": "full time",
            "location": "remote",
            "technologies": ["Python", "Networking", "Linux", "Docker", "Flask", "SQL"],
        },
        "Embedded Software Developer": {
            "company": "Luxoft",
            "type": "full time",
            "location": "remote",
            "technologies": ["Linux", "C", "Networking", "Python"],
        },
    },
    "education": {
        "Cybersecurity Msc.": {
            "type": "master",
            "institution": "UTCN",
            "timeline": (2022, 2024),
        },
        "Bachelor Computer Science": {
            "type": "bachelor",
            "institution": "UTCN",
            "timeline": (2017, 2021),
        },
    },
}

if __name__ == "__main__":
    target_file = open("cv.obj", "wb")
    pickle.dump(stored_data, target_file)
    target_file.close()
