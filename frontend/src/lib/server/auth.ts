import type { RequestEvent} from '@sveltejs/kit'
import { API_BASE_URL } from "$env/static/private";

export {
  do_login_request,

};

async function do_login_request(event:RequestEvent): Promise<Response> {
    
  const API_LOGIN_URL = `${API_BASE_URL}/auth/token`;
  const data = await event.request.formData();

  const body = new URLSearchParams();
  body.append("grant_type", "password");
  body.append("username", data.get("username") as string);
  body.append("password", data.get("password") as string);
  body.append("scope", data.get("scope") as string);
  body.append("client_id", "string") //TODO
  body.append("client_secret", "string")

  return await event.fetch(API_LOGIN_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "accept": "application/json"
    },
    body
  });
};