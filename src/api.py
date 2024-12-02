from crossref.restful import Works

works = Works()

mappings = {
    "author": "author",
    "title": "title",
    "journal": "journal",
    "year": "year"
}

def fetch_work(doi):
    work = works.doi(doi)
    #ARTICLE
    if "author" in work:
        work["author"] = fix_names(work["author"])
    if "container-title" in work and len(work["container-title"]) != 0:
        work["journal"] = work["container-title"][0]
    if "published-print" in work:
        work["year"] = work["published"]["date-parts"][0][0]
        work["month"] = work["published"]["date-parts"][0][1]
    if "published" in work:
        work["year"] = work["published-print"]["date-parts"][0][0]
        work["month"] = work["published-print"]["date-parts"][0][1]
    if "title" in work:
        work["title"] = work["title"][0]
    if "issue" in work:
        work["number"] = work["journal-issue"]["issue"]
    if "page" in work:
        work["pages"] = work["page"]
    #BOOK
    if "editor" in work:
        work["editor"] = fix_names(work["editor"])
    if work["type"] == "monograph":
        work["editor"] = work["author"]

    return work

def fix_names(authors):
    new_author = []
    for author in authors:
        given = author["given"]
        family = author["family"]
        new_author.append(f"{family}, {given}")
    return new_author


#if __name__ == "__main__":
    #print(fetch_work("10.1145/3603178"))
    #print(fetch_work("10.1145/3617291"))
    #print(fetch_work("10.1145/3548732"))
