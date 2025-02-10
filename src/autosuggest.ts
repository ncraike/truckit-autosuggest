const API = 'http://localhost:8080';

export async function lookupCategory(item: string): Promise<string | null> {
    let url = new URL("/autosuggest", API);
    url.searchParams.set("query", item);
    console.log(`Looking up ${item} from URL ${url}`);

    const response = await fetch(url);
    const data = await response.json();
    const message = data["message"];
    if (typeof (message) == "string") {
        return message;
    }
    return null;
}