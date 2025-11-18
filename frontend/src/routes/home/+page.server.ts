import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";
import { API_BASE_URL } from "$env/static/private";


export const load: PageServerLoad = async({cookies, fetch}) => {
    
    const API_VALIDATE_USER_URL = `${API_BASE_URL}auth/me`

    const token = cookies.get("access_token");
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
        cookies.delete("access_token", { path: "/"});
    }

    const user = await res.json();
    
    return { user }
};