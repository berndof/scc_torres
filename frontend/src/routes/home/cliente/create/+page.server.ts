import { API_BASE_URL } from '$env/static/private';
import type { Actions } from './$types';

function emptyToNull(value: any) {
    if (value === null || typeof value === 'undefined') {
        return null; // Mantém null/undefined como null
    }
    // Converte string vazia ou string com apenas espaços em null
    if (typeof value === 'string' && value.trim() === '') {
        return null;
    }
    return value;
}

export const actions = {
    default: async (event) => {
        const formData = await event.request.formData()
    
        //console.log(formData)

        //montar o payload
        const pessoa_payload = {
            "first_name": formData.get("first-name"),
            "last_name": formData.get("last-name"),
            "cpf": formData.get("cpf"),
            
            //fomatar o telefone ?
        
            "telefone": emptyToNull(formData.get("telefone")),
            "email": emptyToNull(formData.get("email")),
            /* "endereco":  */
        }

        const endereco_payload = {
            "logradouro": emptyToNull(formData.get("logradouro")),
            "numero": emptyToNull(formData.get("numero")),
            "bairro": emptyToNull(formData.get("bairro")),
            "cidade": emptyToNull(formData.get("cidade")),
            "estado": emptyToNull(formData.get("estado")),
            "cep": emptyToNull(formData.get("cep"))
        }


        console.log(pessoa_payload, endereco_payload)

        const api_url = `${API_BASE_URL}/clientes/create/pf`

        const res = await event.fetch(api_url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                //TODO add token
            },
            body: JSON.stringify(pessoa_payload)
        });

        if (res.ok) {
            //pegar a mensagem
        }

        const resdata = await res.json()
        console.log(resdata)
        
    }
} satisfies Actions;