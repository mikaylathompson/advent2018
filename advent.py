import click
import requests

def download_input(day, year, cookie_value):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies=dict(session=cookie_value))
    r.raise_for_status()
    return r.text

@click.command()
@click.option('-d', '--day', prompt=True, type=int)
@click.option('-y', '--year', default=2018, type=int)
@click.option('--cookie-file', default=".cookie", type=click.File('r'))
@click.option('--output-file', type=click.File('w'))
def download(day, year, cookie_file, output_file):
    cookie_value = cookie_file.read().strip()
    if not output_file:
        output_file = open(f"day{day}_{year}.txt", 'w')
    output_file.write(download_input(day, year, cookie_value))
    output_file.close()



    

if __name__ == '__main__':
    download()

