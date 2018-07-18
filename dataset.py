from torch.utils.data import DataLoader, Dataset

__build__ = 2018
__author__ = "singsam_jam@126.com"


def get_loader(args, kwargs):
    train_loader = DataLoader(dataset=ModelDataset, batch_size=args.test_batch_size, collate_fn=collate_fn, shuffle=True,
                              **kwargs)
    test_loader = DataLoader(dataset=ModelDataset, batch_size=args.test_batch_size, collate_fn=collate_fn, shuffle=False,
                             **kwargs)

    return train_loader, test_loader

class ModelDataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        item = None
        return item

    def __len__(self):
        raise NotImplementedError

def collate_fn():
    pass
