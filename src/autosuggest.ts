const BACKEND = 'http://localhost:8080';

export async function lookup(item: string): Promise<any> {
    let url = new URL("/autosuggest", BACKEND);
    url.searchParams.set("query", item);
    console.log(`Looking up ${item} from URL ${url}`);

    const response = await fetch(url);
    const data = await response.json();
    const message = data["message"];
    return message;
}