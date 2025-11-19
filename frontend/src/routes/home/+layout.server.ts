import { error, redirect } from "@sveltejs/kit";
import type { LayoutServerLoad, RequestEvent } from "./$types";
import { API_BASE_URL } from "$env/static/private";

const API_VALIDATE_USER_URL = `${API_BASE_URL}/auth/me`

export const load: LayoutServerLoad = async(event) => {
      
    const token = event.cookies.get("access_token");
    if (!token) {
        throw redirect(302, "/login") 
    };

    //valida token no backend
    const res = await fetch(API_VALIDATE_USER_URL, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });

    if (!res.ok) {
        event.cookies.delete("access_token", { path: "/"});
    }

    const user = await res.json();

    //TODO montar o data que é o contexto do frontend - e dos componentes como sidebar e header

    return {
        user: user,
    }
};