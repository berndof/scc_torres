import type { Actions } from './$types';

export const actions = {
    login: async ({ request }) => {
        const formData = await request.formData();

        const username = formData.get('username')?.toString();
        const password = formData.get('password')?.toString();
        const scope = formData.get('scope')?.toString();

        console.log(formData)

    }
} satisfies Actions