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
    work["author"] = fix_names(work["author"])
    work["journal"] = work["container-title"][0]
    if work["published-print"]:
        work["year"] = work["published"]["date-parts"][0][0]
    else:
        work["year"] = work["published-print"]["date-parts"][0][0]
    work["title"] = work["title"][0]

    return work

def fix_names(authors):
    new_author = []
    for author in authors:
        given = author["given"]
        family = author["family"]
        new_author.append(f"{family}, {given}")
    return new_author


if __name__ == "__main__":
    print(fetch_work("10.1109/MSPEC.2016.7439593"))
    