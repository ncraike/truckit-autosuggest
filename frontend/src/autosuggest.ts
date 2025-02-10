const API_URL = __AUTOSUGGEST_API_URL__;

export async function lookupCategory(item: string): Promise<string | null> {
    let url = new URL('/autosuggest', API_URL);
    url.searchParams.set('query', item);

    try {
        const response = await fetch(url);
        const data = await response.json();
        const message = data['message'];
        if (typeof message == 'string') {
            return message;
        }
        return null;
    } catch (error: unknown) {
        if (error instanceof Error) {
            console.error(error.message);
        } else {
            console.error('Error looking up category');
        }
        return null;
    }
}
