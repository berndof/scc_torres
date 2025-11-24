<script lang="ts">
    import DataTable from "./data-table.svelte";
    import { columns } from "./columns.ts";
    
    let { data } = $props();
</script>
 
<DataTable data={data.payments} {columns} />