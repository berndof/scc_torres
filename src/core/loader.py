import pkgutil
from importlib import import_module
from pathlib import Path

APPS_ROOT_DIR = Path(__file__).parent.parent / "apps"
# /app1 /submodule app1/models.py esse é o modulo que preciso importar agora


def load_modules(models: bool = False, routers: bool = False):
    if not models and not routers:
        return

    for (
        _,
        app_name,
        ispkg,
    ) in pkgutil.iter_modules([str(APPS_ROOT_DIR)]):
        if not ispkg:
            continue
        subpkgs_path = Path(APPS_ROOT_DIR / app_name)

        for _, subpgk_name, ispkg in pkgutil.iter_modules([str(subpkgs_path)]):
            if not ispkg:
                continue

            modules_path = Path(subpkgs_path / subpgk_name)
            prefix = f"apps.{app_name}.{subpgk_name}"

            # debug
            # print(f"📦 {prefix} -> {modules_path}")

            for file in modules_path.iterdir():
                # print(file.stem)
                if not file.is_file() or not file.suffix == ".py":
                    continue

                if models and file.stem == "model":
                    try:
                        import_module(f"{prefix}.model")
                        # print(f"✅ importado: {prefix}.model")
                    except ModuleNotFoundError:
                        pass
                    except Exception as e:
                        # print(f"⚠️ erro importando {prefix}.model: {e}")
                        ...
                if routers and file.stem == "routes":
                    try:
                        import_module(f"{prefix}.routes")
                        # print(f"✅ importado: {prefix}.routes")
                    except ModuleNotFoundError:
                        pass
                    except Exception as e:
                        # print(f"⚠️ erro importando {prefix}.routes: {e}")
                        ...
