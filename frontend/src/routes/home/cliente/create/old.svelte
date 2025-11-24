<script lang="ts">
    import * as Form from "$lib/components/ui/form";
    import { Input } from "$lib/components/ui/input";
    import { Select, SelectTrigger, SelectContent, SelectItem } 
        from "$lib/components/ui/select";

    import { superForm } from "sveltekit-superforms";
    import { zod4Client } from "sveltekit-superforms/adapters";

    import { newClienteSchema } from "./oldschema.js";

    export let data;

    const form = superForm(data.form, {
        validators: zod4Client(newClienteSchema)
    });

    const { form: formData, enhance } = form;
</script>
<form method="POST" use:enhance class="space-y-6 max-w-md">

  <!-- NOME -->
  <Form.Field {form} name="nome">
    <Form.Control>
      {#snippet children({ props })}
        <Form.Label>Nome</Form.Label>
        <Input {...props} bind:value={$formData.nome} />
      {/snippet}
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>

    <!-- TIPO -->
    <Form.Field {form} name="tipo">
    <Form.Control>
        {#snippet children({ props })}
        <Form.Label>Tipo</Form.Label>

        <Select type="single" {...props} bind:value={$formData.tipo}>
            <SelectTrigger>
            {$formData.tipo || "Selecione o tipo..."}
            </SelectTrigger>

            <SelectContent>
            <SelectItem value="PF">Pessoa Física</SelectItem>
            <SelectItem value="PJ">Pessoa Jurídica</SelectItem>
            </SelectContent>
        </Select>
        {/snippet}
    </Form.Control>
    <Form.FieldErrors />
    </Form.Field>

  {#if $formData.tipo === 'PF'}
    <Form.Field {form} name="cpf">
      <Form.Control>
        {#snippet children({ props })}
          <Form.Label>CPF</Form.Label>
          <Input {...props} bind:value={$formData.cpf} />
        {/snippet}
      </Form.Control>
      <Form.FieldErrors />
    </Form.Field>
  {/if}

  {#if $formData.tipo === 'PJ'}
    <Form.Field {form} name="cnpj">
      <Form.Control>
        {#snippet children({ props })}
          <Form.Label>CNPJ</Form.Label>
          <Input {...props} bind:value={$formData.cnpj} />
        {/snippet}
      </Form.Control>
      <Form.FieldErrors />
    </Form.Field>
  {/if}

  <Form.Button type="submit">Criar</Form.Button>
</form>