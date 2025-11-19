// src/routes/clientes/novo/schema.ts
import { z } from "zod";

export const newClienteSchema = z.object({
    nome: z.string().min(2, "Mínimo de 2 caracteres"),
    tipo: z.enum(["PF", "PJ"]),
    cpf: z.string().optional(),
    cnpj: z.string().optional()
})
.refine((d) => d.tipo === "PF" ? !!d.cpf : true, {
    message: "CPF obrigatório",
    path: ["cpf"]
})
.refine((d) => d.tipo === "PJ" ? !!d.cnpj : true, {
    message: "CNPJ obrigatório",
    path: ["cnpj"]
});

export type NewClienteSchema = typeof newClienteSchema;
