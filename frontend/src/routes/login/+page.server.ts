import type { Actions } from './$types';
import { redirect, fail} from '@sveltejs/kit';
import { do_login_request } from "$lib/server/auth"

export const actions = {
    login: async (event) => {
    const res = await do_login_request(event)
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