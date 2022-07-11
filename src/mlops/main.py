import hydra
from omegaconf import DictConfig, OmegaConf
from src.train import Pipe
@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    pipe = Pipe()
    if cfg.preprocess:
        pipe.preprocess()
    if cfg.train:
        pipe.train()

if __name__ == "__main__":
    main()
