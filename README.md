# House Party Translation Project

## About

This project aims to translate all of the dialog in the game House Party into other languages using AI. The project is written in Python and uses a variety of machine translation and natural language processing techniques to produce high-quality translations.

**Note:** This project is still under development and is not yet 100% complete.

## Installation

To install the project, simply clone the repository and run the following command:

TODO...

## Usage

To use the project, follow some simply steps:

Download original files to translate from their servers:
https://games.eekllc.com/Download/stories/Mods.[version].zip

> Example: https://games.eekllc.com/Download/stories/Mods.1.3.0.zip

Put the extracted zip content in /original/[version]/ folder.

> Example: /original/1.3.0/

Run the following command:

`python HousePartyTranslator.py`

## Contributing

Contributions are welcome! If you would like to contribute to the project, please fork the repository and create a pull request.

## License

The project is licensed under the MIT License.

## Acknowledgments

The project is a work in progress and is still under development.

## Contact

If you have any questions or feedback, please contact me at johnngoes@gmail.com.

## Known Issues

The project is still under development and there are a few known issues:

- The code actually wont translate anythin, only create files for organize the data to make prompts.
- I had some issues with asking AI to translate chunks of original files.

## TODO

- Create prompt to translate X amount of lines without loosing the bound with translation ID.
- Create routine to translate chunks of lines and update json files.
- Create function to create finished translated files based on original format.
- Create installation function to install all requiriments.