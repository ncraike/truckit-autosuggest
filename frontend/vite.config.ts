import { defineConfig } from 'vite'

const fromEnvWithDefault = (envVarName: string, defaultValue: string): string => (
    JSON.stringify(process.env[envVarName] || defaultValue)
);

export default defineConfig({
    define: {
        __AUTOSUGGEST_API_URL__: fromEnvWithDefault('AUTOSUGGEST_API_URL', 'http://localhost:7000'),
    }
})