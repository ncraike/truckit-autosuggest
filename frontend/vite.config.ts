import { defineConfig } from 'vite'

const fromEnvWithDefault = (envVarName: string, defaultValue: string): string => (
    process.env[envVarName] || defaultValue
);

const intFromEnvWithDefault = (envVarName: string, defaultValue: number): number => (
    process.env[envVarName] && parseInt(process.env[envVarName]) || defaultValue
)

export default defineConfig({
    define: {
        // Values here have to be stringified as they're substituted raw
        __AUTOSUGGEST_API_URL__: JSON.stringify(fromEnvWithDefault('AUTOSUGGEST_API_URL', 'http://localhost:7000')),
    },
    server: {
        host: fromEnvWithDefault("LISTEN_HOST", "localhost"),
        port: intFromEnvWithDefault("LISTEN_PORT", 8000),
    },
})