import camelcaseKeys from "camelcase-keys"

export const getInfoFromJWTToken = (token: string) => {
    const tokenPayload = token.split('.')[1]
    const decodedPayload = atob(tokenPayload)
    console.log(camelcaseKeys(JSON.parse(decodedPayload), { deep: true }))
    return camelcaseKeys(JSON.parse(decodedPayload), { deep: true })
}
