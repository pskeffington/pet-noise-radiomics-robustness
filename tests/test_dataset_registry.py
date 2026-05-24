import importlib.util
from pathlib import Path


MODULE_PATH = Path("analysis/00_validate_dataset_registry.py")


def load_validator_module():
    spec = importlib.util.spec_from_file_location("dataset_registry_validator", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_dataset_registry_validates():
    module = load_validator_module()
    registry = module.validate_registry()
    assert len(registry) >= 1
    assert registry["dataset_id"].is_unique
    assert "fdg_pet_ct_lesions" in set(registry["dataset_id"])
