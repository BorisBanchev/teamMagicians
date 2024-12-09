function check(form) {
    if (form.keyword.value.length > 20) {
        alert("Reference keyword length can't be greater than 20");
        return false;
    }
    if (form.keyword.value.length == 0) {
        alert("Reference keyword length can't be empty");
        return false;
    }
    if (form.author.value.length < 3 && form.author.value.length > 0) {
        alert("Reference author length must be greater than 2");
        return false;
    }
    if (
        (form.title.value.length > 100 || form.title.value.length < 3) &&
        form.title.value.length > 0
    ) {
        alert(
            "Reference title length must be smaller than 100 and greater than 2"
        );
        return false;
    }
    if (form.journal.value.length < 3 && form.journal.value.length > 0) {
        alert("Reference journal length must be greater than 2");
        return false;
    }
    if (
        (parseInt(form.year.value) <= 0 || parseInt(form.year.value) > 2024) &&
        form.year.value.length > 0
    ) {
        alert("Reference year must be positive and smaller than 2025");
        return false;
    }
}

const referenceFields = {
    article: {
        mandatory: ["author", "title", "journal", "year"],
        optional: ["volume", "number", "pages", "month", "note"],
    },
    book: {
        mandatory: ["author", "title", "publisher", "editor", "year"],
        optional: [
            "volume",
            "number",
            "series",
            "type",
            "chapter",
            "pages",
            "address",
            "edition",
            "month",
            "note",
        ],
    },
    misc: {
        mandatory: [],
        optional: ["author", "title", "howpublished", "month", "year", "note"],
    },
    inproceedings: {
        mandatory: ["author", "title", "booktitle", "year"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "pages",
            "address",
            "month",
            "organization",
            "publisher",
        ],
    },
    booklet: {
        mandatory: ["author", "title", "howpublished", "year", "address"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "organization",
            "month",
            "note",
        ],
    },
    conference: {
        mandatory: ["author", "title", "booktitle", "year"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "pages",
            "address",
            "month",
            "organization",
            "publisher",
            "note",
        ],
    },
    inbook: {
        mandatory: ["author", "title", "booktitle", "publisher", "year"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "address",
            "edition",
            "month",
            "pages",
            "note",
        ],
    },
    incollection: {
        mandatory: ["author", "title", "booktitle", "publisher", "year"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "pages",
            "address",
            "month",
        ],
    },
    manual: {
        mandatory: ["title", "year"],
        optional: [
            "author",
            "organization",
            "address",
            "edition",
            "month",
            "note",
        ],
    },
    mastersthesis: {
        mandatory: ["author", "title", "school", "year"],
        optional: ["type", "address", "month", "note"],
    },
    phdthesis: {
        mandatory: ["author", "title", "school", "year"],
        optional: ["type", "address", "month", "note"],
    },
    proceedings: {
        mandatory: ["title", "year"],
        optional: [
            "editor",
            "volume",
            "number",
            "series",
            "address",
            "month",
            "publisher",
        ],
    },
    techreport: {
        mandatory: ["author", "title", "institution", "year"],
        optional: ["type", "number", "address", "month", "note"],
    },
    unpublished: {
        mandatory: ["author", "title", "note"],
        optional: ["month", "year"],
    },
};
const updateFormFields = (modify) => {
    const type = document.getElementById("reference_type").value;
    const fields = referenceFields[type];
    const formFieldsDiv = document.getElementById("form-fields");
    formFieldsDiv.innerHTML = "";

    // mandatory fields
    const mandatory = modify ? [...fields.mandatory] : ["keyword", ...fields.mandatory];
    const mandatoryDiv = document.createElement("div");
    mandatoryDiv.classList.add("field_group");
    mandatoryDiv.classList.add("required");
    for (const field of mandatory) {
        mandatoryDiv.appendChild(createField(field, true, modify));
    }
    formFieldsDiv.appendChild(mandatoryDiv);
    const separator = document.createElement("div");
    separator.classList.add("separator");
    formFieldsDiv.appendChild(separator);

    // optional fields
    const optionalDiv = document.createElement("div");
    optionalDiv.classList.add("field_group");
    optionalDiv.classList.add("optional");
    for (const field of fields.optional) {
        optionalDiv.appendChild(createField(field, false, modify));
    }
    formFieldsDiv.appendChild(optionalDiv);
};

const createField = (field, required, modify) => {
    const row = document.createElement("div");
    row.classList.add("row");
    row.classList.add(required ? "required" : "optional");

    const label = document.createElement("label");
    label.setAttribute("for", field);
    label.innerText = (
        field.charAt(0).toUpperCase() +
        field.slice(1) +
        ":"
    ).replace(/_/g, " ");

    const input = document.createElement("input");
    input.type = "text";
    if (modify) input.value = data[field];
    input.name = field;
    input.id = field;
    input.required = required;
    row.appendChild(label);
    row.appendChild(input);
    return row;
};
