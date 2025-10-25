import os
from torch_geometric.datasets import TUDataset

def download_datasets():
    """Download graph datasets to datasets folder"""
    datasets_list = ["AIDS", "PROTEINS", "NCI1", "PTC_MR", "MUTAG"]
    datasets_path = os.path.join(os.path.dirname(__file__), "..", "datasets")
    
    # Create datasets directory if it doesn't exist
    os.makedirs(datasets_path, exist_ok=True)
    
    for dataset_name in datasets_list:
        print(f"Downloading {dataset_name}...")
        try:
            dataset = TUDataset(root=datasets_path, name=dataset_name)
            print(f"✓ {dataset_name} downloaded successfully")
        except Exception as e:
            print(f"✗ Error downloading {dataset_name}: {e}")

if __name__ == "__main__":
    download_datasets()