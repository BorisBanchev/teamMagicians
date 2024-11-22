class UserInputError(Exception):
    pass

def validate_reference(reference_type, fields):
    reference_fields = {
        "article": {"mandatory": ["author", "title", "journal", "year"], "optional": ["volume", "number", "pages", "month", "note"]},
        "book": {"mandatory": ["author", "title", "publisher", "year"], "optional": ["editor", "volume", "number", "series", "edition", "isbn"]},
        "misc": {"mandatory": [], "optional": ["author", "title", "howpublished", "month", "year", "note"]},
    }

    if reference_type not in reference_fields:
        raise ValueError("Invalid reference type selected.")

    # Check mandatory fields
    missing_fields = [
        field for field in reference_fields[reference_type]["mandatory"] if not fields.get(field)
    ]
    
    if missing_fields:
        raise ValueError(f"Missing mandatory fields: {', '.join(missing_fields)}")
    
    #Check that at least one field is maintained


    if "author" in fields and len(fields["author"]) < 3:
        raise UserInputError("Reference author length must be greater than 2")
    
    if "title" in fields and len(fields["title"]) < 3 or len(fields["title"]) > 100:
        raise UserInputError("Reference title length must be smaller than 100 and greater than 2")
    
    if "journal" in fields and len(fields["journal"]) < 3:
        raise UserInputError("Reference journal length must be greater than 2")
    
    if "year" in fields and int(fields["year"]) <= 0 or int(fields["year"]) > 2025:
        raise UserInputError("Reference year must be positive and smaller than 2026")


def raise_error(message):
    raise UserInputError(message)

