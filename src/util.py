class UserInputError(Exception):
    pass


def validate_reference(author, title, journal, year):
    if len(author) == 0 or len(author) < 3:
        raise UserInputError("Reference author length can not be empty or must be greater than 2")
    
    if len(title) > 100:
        raise UserInputError("Reference title length must be smaller than 100")
    
    if len(journal) == 0 or len(journal) < 3:
        raise UserInputError("Reference journal length can not be empty or must be greater than 2")
    
    if year <= 0 or year > 2025:
        raise UserInputError("Reference year must be positive and smaller than 2026")

    