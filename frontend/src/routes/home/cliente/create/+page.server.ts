// src/routes/clientes/novo/+page.server.ts
import { superValidate, fail } from "sveltekit-superforms";
import { zod4 } from "sveltekit-superforms/adapters";
import { newClienteSchema } from "./schema";

export const load = async () => {
    return {
        form: await superValidate(null, zod4(newClienteSchema))
    };
};

export const actions = {
    default: async (event) => {
        const form = await superValidate(event, zod4(newClienteSchema));

        if (!form.valid) {
            return fail(400, { form });
        }

        // Persistência de verdade aqui
        // await db.cliente.create({ data: form.data });

        return { form };
    }
};
