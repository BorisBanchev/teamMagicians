class UserInputError(Exception):
    pass

reference_fields = {
    "article": {"mandatory": ["author", "title", "journal", "year"],
                "optional": ["volume", "number", "pages", "month", "note"]},
    "book": {"mandatory": ["author", "title", "publisher", "year"],
                "optional": ["editor", "volume", "number", "series", "edition", "isbn"]},
    "misc": {"mandatory": [],
                "optional": ["author", "title", "howpublished", "month", "year", "note"]},
    "inproceedings": {"mandatory": ["author", "title", "booktitle", "year"],
                        "optional": ["editor", "volume", "number", "series", "pages",
                                    "address", "month", "organization", "publisher"]},
    "booklet": {"mandatory": ["author", "title", "howpublished", "year", "address"],
                "optional": ["editor", "volume", "number", "series",
                                "organization", "month", "note"]},
    "conference": {"mandatory": ["author", "title", "booktitle", "year"],
                    "optional": ["editor", "volume", "number", "series", "pages",
                                "address", "month", "organization", "publisher", "note"]},
    "inbook": {"mandatory": ["author", "title", "booktitle", "publisher", "year"],
                "optional": ["editor", "volume", "number", "series", "address", "edition",
                            "month", "pages", "note"]},
    "incollection": {"mandatory": ["author", "title", "booktitle", "publisher", "year"],
                        "optional": ["editor", "volume", "number", "series", "pages", "address", "month"]},
    "manual": {"mandatory": ["title", "year"],
                "optional": ["author", "organization", "address", "edition", "month", "note"]},
    "mastersthesis": {"mandatory": ["author", "title", "school", "year"],
                        "optional": ["type", "address", "month", "note"]},
    "phdthesis": {"mandatory": ["author", "title", "school", "year"],
                    "optional": ["type", "address", "month", "note"]},
    "proceedings": {"mandatory": ["title", "year"],
                    "optional": ["editor", "volume", "number", "series", "address", "month", "publisher"]},
    "techreport": {"mandatory": ["author", "title", "institution", "year"],
                    "optional": ["type", "number", "address", "month", "note"]},
    "unpublished": {"mandatory": ["author", "title", "note"],
                    "optional": ["month", "year"]}
}


def validate_reference(reference_type, fields):
    if not fields["keyword"]:
        raise ValueError("Keyword is a mandatory field")

    fields_for_type = reference_fields[reference_type]

    # Check mandatory fields
    missing_fields = [
        field for field in fields_for_type["mandatory"] if not fields.get(field)
    ]

    if missing_fields:
        raise ValueError(f"Missing mandatory fields: {', '.join(missing_fields)}")

    #Check that at least one field is maintained (case misc)
    all_valid_fields = fields_for_type["mandatory"] + fields_for_type["optional"]
    provided_fields = [
        field for field in all_valid_fields if fields.get(field)
    ]

    if not provided_fields:
        raise ValueError("At least one field needs to be maintained.")

    rules = {
        "keyword": (0, 20, "Reference keyword length can't be greater than 20"),
        "address": (3, 100, "Reference address length must be between 3 and 100"),
        "author": (3, 1000, "Reference author length must be between 3 and 1000"),
        "booktitle": (3, 100, "Reference booktitle length must be between 3 and 100"),
        "howpublished": (3, 100, "Reference howpublished length must be between 3 and 100"),
        "institution": (3, 100, "Reference institution length must be between 3 and 100"),
        "journal": (3, 100, "Reference journal length must be between 3 and 100"),
        "note": (3, 100, "Reference journal length must be between 3 and 100"),
        "publisher": (3, 100, "Reference publisher length be between 3 and 100"),
        "school": (3, 100, "Reference school length must be between 3 and 100"),
        "title": (3, 100, "Reference title length must be between 3 and 100")
    }

    for field, constraint in rules.items():
        if field in fields:
            min_length, max_length, error_message = constraint
            if check_input_length(fields[field], min_length) or len(fields[field]) > max_length:
                raise ValueError(error_message)

    if "year" in fields:  # Check if year exists and is not empty
        if fields["year"] == "":
            pass
        elif int(fields["year"]) < 0 or int(fields["year"]) > 2024:  # Check range
            raise ValueError("Reference year must be positive and smaller than 2025")

def check_input_length(field, min_length):
    return len(field) > 0 and len(field) < min_length

def check_valid_keyword(keyword, list_keywords):
    if keyword in list_keywords:
        raise  ValueError("Reference keyword must be unique")

def raise_error(message):
    raise ValueError(message)
