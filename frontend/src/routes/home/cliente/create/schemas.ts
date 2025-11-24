import { z } from "zod";

export const pfSchema = z.object({
  nome: z.string().min(1),
  cpf: z.string().min(11).max(11), // ajustar validação
});

export const pjSchema = z.object({
  nome: z.string().min(1),
  cnpj: z.string().min(14).max(14), // ajustar validação
});