import { redirect } from '@sveltejs/kit';
import type { Actions } from './$types.js'

export const actions = {
    default: async ({ cookies }) => {
        cookies.delete('access_token', {
            path: '/'
        });

        throw(redirect(302, '/login'));
    }
} satisfies Actions;
