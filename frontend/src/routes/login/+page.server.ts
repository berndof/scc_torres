import type { Actions } from './$types';
import { redirect, fail} from '@sveltejs/kit';
import { API_BASE_URL } from '$env/static/private';

export const actions = {
    login: async (event) => {
  
      const API_LOGIN_URL = `${API_BASE_URL}/auth/token`;
      const formData = await event.request.formData();

    const body = new URLSearchParams();
    body.append("grant_type", "password");
    body.append("username", formData.get("username") as string);
    body.append("password", formData.get("password") as string);
    body.append("scope", formData.get("scope") as string);
    body.append("client_id", "string") //TODO
    body.append("client_secret", "string")

    const res = await event.fetch(API_LOGIN_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
      },
      body
    });
    const data = await res.json();
    //tratar resposta
    if (!res.ok) {
      return fail(res.status, { error: data.detail });
    };

    event.cookies.set("access_token", data.access_token, {
      path: '/',
      httpOnly: true, 
      sameSite: 'strict', 
      secure: false
    });

    //salvei o bearer token nos cookies 

    throw redirect(302, '/home')

    }
} satisfies Actions