// import './style.css'

import { lookupCategory } from "./autosuggest";

export function setupForm(form: HTMLFormElement) {
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        submitForm(form);
    });
}

export async function submitForm(form: HTMLFormElement) {
    const formData = new FormData(form);
    const query = formData.get("query")
    if (query) {
        const response = await lookupCategory(query.toString());
        const responseElement = document.querySelector("#response");
        if (response && responseElement) {
            responseElement.innerHTML = response;
        }
    }
}

setupForm(document.querySelector<HTMLFormElement>('#lookupForm')!);