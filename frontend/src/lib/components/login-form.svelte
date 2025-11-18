<script lang="ts">
	import { Button } from "$lib/components/ui/button/index.js";
	import * as Select from "$lib/components/ui/select/index.js";
	import * as Card from "$lib/components/ui/card/index.js";

	import {
		FieldGroup,
		Field,
		FieldLabel,
		FieldDescription,
		FieldSeparator,
	} from "$lib/components/ui/field/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { cn } from "$lib/utils.js";
	import type { HTMLAttributes } from "svelte/elements";

	//let form;


    // Pegamos TODOS os props numa tacada só
    const allProps = $props();

    // Extrair props customizados primeiro
    export const form = allProps.form;

    // Remover o form do objeto para o restProps não carregá-lo
    const { form: _ignore, class: className, ...restProps } =
        allProps as HTMLAttributes<HTMLDivElement> & { form?: unknown };


	//let { class: className, ...restProps }: HTMLAttributes<HTMLDivElement> = $props();

	const id = $props.id();

	let username = $state("");
	let password = $state("");
	let scope = $state("local");



</script>

<div class={cn("flex flex-col gap-6", className)} {...restProps}>
	<Card.Root>
		<Card.Header class="text-center">
			<Card.Title class="text-xl"> Bem vindo</Card.Title>
			<!-- <Card.Description>Login with your Apple or Google account</Card.Description>-->
		</Card.Header>
		<Card.Content>
			<form method="POST" action="?/login">
				<FieldGroup>
					<Field>
						<FieldLabel for="username-{id}">Username</FieldLabel>
						<Input 
							id="username-{id}"
							name="username"
							type="text"
							placeholder="username"
							bind:value={username}
							required 
						/>
					</Field>
					<Field>
						<FieldLabel for="password-{id}">Password</FieldLabel>
						<!-- <a href="##" class="ml-auto text-sm underline-offset-4 hover:underline">
							Forgot your password?
						</a> -->
						<Input
						 	id="password-{id}"
							name="password"
							type="password"
							bind:value={password}
							required 
						/>
					</Field>
					<Field>
						<Button type="submit">Login</Button>
						<!-- <FieldDescription class="text-center">
							Don't have an account? <a href="##">Sign up</a>
						</FieldDescription> -->
					</Field>
					
					<Field class="flex flex-col items-center mt-4">
						<!-- Select centralizado abaixo do botão -->
						<Select.Root type="single" name="scope" bind:value={scope}>

							<Select.Trigger class="w-full max-w-[200px] text-center">
								{scope === "local" ? "Local" : "LDAP"}
							</Select.Trigger>

							<Select.Content>
								<Select.Item value="local">Local</Select.Item>
								<Select.Item value="ldap">LDAP</Select.Item>
							</Select.Content>
						</Select.Root>

					</Field>
					
				</FieldGroup>
			</form>
		</Card.Content>
	</Card.Root>
	<!-- <FieldDescription class="px-6 text-center">
		By clicking continue, you agree to our <a href="##">Terms of Service</a>
		and <a href="##">Privacy Policy</a>.
	</FieldDescription> -->
</div>
