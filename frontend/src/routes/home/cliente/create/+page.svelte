<script lang="ts">
    import { Button } from "$lib/components/ui/button/index.js";
    import FieldSet from "$lib/components/ui/field/field-set.svelte";
    import { Field, FieldGroup, FieldLabel, FieldLegend, FieldDescription, FieldSeparator} from "$lib/components/ui/field/index.js";
    import { Input } from "$lib/components/ui/input";
    import { Separator } from "$lib/components/ui/separator/index.js";
    import { Card, CardHeader, CardTitle, CardContent }from "$lib/components/ui/card/index.js";
    import * as Select from "$lib/components/ui/select/index.js";
    //export let data;

    let tipo: "PF" | "PJ" | ""  = "";

    // dados do form
    const clienteTipo = [
        {value: "pj", label: "Pessoa Jurídica"},
        {value: "pf", label: "Pessoa Física"},
    ];

    let form_tipo_estado = $state("pf");

    const triggerContent = $derived(
    clienteTipo.find((t) => t.value === form_tipo_estado)?.label ?? "Tipo do cliente"
  );

   let mostrar_endereco = $state(false);
</script>

<!-- Seleção de tipo -->
<div class="mb-4">
    <label for="cliente_tipo" class="block mb-1 font-medium text-sm text-gray-700">
        Tipo do Cliente
    </label>
    <Select.Root type="single" name="cliente_tipo" bind:value={form_tipo_estado}>
    <Select.Trigger class="w-[180px]">
        {triggerContent}
    </Select.Trigger>
    <Select.Content>
        <Select.Group>
        <!-- <Select.Label>Tipo do Cliente</Select.Label> -->
        {#each clienteTipo as tipo (tipo.value)}
            <Select.Item
            value={tipo.value}
            label={tipo.label}
            >
            {tipo.label}
            </Select.Item>
        {/each}
        </Select.Group>
    </Select.Content>
    </Select.Root>
</div>


<Card class="w-full">

    <CardHeader>
<!-- <div class="mt-4 p-4 border border-gray-300 rounded-lg bg-gradient-to-r from-gray-50 to-gray-100 shadow-sm"> -->
    <!-- <h2 class="font-medium mb-2">Pessoa Física</h2> -->
    <CardTitle>Dados do cliente</CardTitle>
    <Separator class="mb-2" />
    <!-- Primeiro FieldGroup: Nome e Sobrenome lado a lado -->
    </CardHeader>
    <CardContent>
        
        {#if form_tipo_estado === "pf"}
        <form method="POST">
        <FieldSet>

            <FieldGroup>
                <div class="grid grid-cols-3 gap-4">
                    <Field aria-required>
                        <FieldLabel for="first-name">Primeiro Nome *</FieldLabel>
                        <Input required id="first-name" name="first-name" placeholder="Nome"/>
                    </Field>

                    <Field aria-required>
                        <FieldLabel for="last-name">Último Nome *</FieldLabel>
                        <Input id="last-name" name="last-name" required />
                    </Field>

                    <Field>
                        <FieldLabel for="cpf">CPF *</FieldLabel>
                        <Input id="cpf" name="cpf" required/>
                    </Field>

                    <Field>
                        <FieldLabel for="telefone">Telefone (opcional)</FieldLabel>
                        <Input id="telefone" name="telefone" />
                    </Field>

                    <Field>
                        <FieldLabel for="email">Email (opcional)</FieldLabel>
                        <Input id="email" name="email" />
                    </Field>
                </div>
            </FieldGroup>

            <!-- Botão para mostrar endereço -->
             <div class="mt-4">
                <Button 
                    type="button"
                    variant="outline"
                    onclick={() => mostrar_endereco = !mostrar_endereco}
                >
                    {mostrar_endereco ? "− Remover endereço" : "+ Adicionar endereço"}
                </Button>
            </div> 

            <!-- Bloco de endereço -->
             {#if mostrar_endereco}
            <div class="mt-4 p-4 rounded-md border bg-gray-50">
                <FieldGroup class="grid grid-cols-3 gap-4">
                    <Field>
                        <FieldLabel for="logradouro">Logradouro</FieldLabel>
                        <Input id="logradouro" name="logradouro" />
                    </Field>

                    <Field>
                        <FieldLabel for="numero">Número</FieldLabel>
                        <Input id="numero" name="numero" />
                    </Field>

                    <Field>
                        <FieldLabel for="bairro">Bairro</FieldLabel>
                        <Input id="bairro" name="bairro" />
                    </Field>

                    <Field>
                        <FieldLabel for="cidade">Cidade</FieldLabel>
                        <Input id="cidade" name="cidade" />
                    </Field>

                    <Field>
                        <FieldLabel for="estado">Estado</FieldLabel>
                        <Input id="estado" name="estado" />
                    </Field>

                    <Field>
                        <FieldLabel for="cep">CEP</FieldLabel>
                        <Input id="cep" name="cep" />
                    </Field>
                </FieldGroup>
            </div>
            {/if}

            <!-- Botão de submit -->
            <div class="mt-6">
                <Button type="submit" class="w-full">
                    Enviar Cadastro PF
                </Button>
            </div>
            </FieldSet>
        </form>

                   
    {:else if form_tipo_estado === "pj"}
    form pj
    {/if} 
    </CardContent>
</Card>

