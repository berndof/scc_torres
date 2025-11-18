<script lang="ts">
	import AppSidebar from "$lib/components/app-sidebar.svelte";
	import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
	import { Separator } from "$lib/components/ui/separator/index.js";
	import * as Sidebar from "$lib/components/ui/sidebar/index.js";
    import { setContext } from "svelte";

    let { children, data, ...restProps } = $props()
    const user = data.user

    // 🔥 deixa o user global no contexto	
    setContext("user", user);

</script>
<Sidebar.Provider>
	<AppSidebar/>
	<Sidebar.Inset>
			{@render children()}
	</Sidebar.Inset>
</Sidebar.Provider>
