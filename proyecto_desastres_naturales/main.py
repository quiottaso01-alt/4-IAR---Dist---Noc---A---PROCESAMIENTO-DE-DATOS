from extract.extract import extract_data
from transform.transform import transform_data
from load.load import load_data

def main():
    url = "https://drive.google.com/uc?export=download&id=1uUD_D1v0HDBrL3y2x947w56tCTN5vFlP"

    # EXTRACT
    df = extract_data(url)

    # TRANSFORM
    df = transform_data(df)

    # LOAD
    load_data(df)

if __name__ == "__main__":
    main()