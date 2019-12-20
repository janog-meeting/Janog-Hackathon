from pathlib import Path
from operator import itemgetter
from typing import Dict, List

from jinja2 import Environment, FileSystemLoader


base_dir = Path.cwd()


class Render:
    """Render connections information to YAML

    Attributes:
        output_path (str)
        template (jinja2.Template)
    """

    def __init__(
        self,
        template_filename: str,
        template_dir: str = f'{base_dir}/templates',
        output_filename: str = 'sample.yml',
        output_dir: str = f'{base_dir}/output'
    ):
        """
        Args:
            template_filename (str):
            template_dir (str, optional): Defaults to f'{base_dir}/templates'.
            output_filename (str, optional): Defaults to ''.
            output_dir (str, optional): Defaults to f'{base_dir}/output'.
        """

        self.output_path = f'{output_dir.rstrip("/")}/{output_filename}'

        template_dir = f'{template_dir.rstrip("/")}'
        env = Environment(loader=FileSystemLoader(template_dir))
        self.template = env.get_template(template_filename)

    def write(self, *args, **kwargs):
        stream = self.template.stream(*args, **kwargs)
        stream.dump(self.output_path, encoding='utf-8')


def parse(cdp_neighbors: Dict[str, List[Dict[str, str]]]):
    """Parse

    Args:
        cdp_neighbors (Dict[str, List[Dict[str, str]]])

    Returns:
        result (List[List[str]])
    """

    result: List[List[str]] = []
    tmp = [
        tuple(sorted([k, d['DST-HOST']]))
        for k, v in cdp_neighbors.items() for d in v
    ]
    tmp = tuple(sorted(set(tmp), key=itemgetter(0)))

    for node1, node2 in tmp:
        edge1 = node1
        for item in cdp_neighbors.get(node2, list()):
            if item['DST-HOST'] == node1:
                edge1 = f'{node1}:{item["SRC-IF"]}'

        edge2 = node2
        for item in cdp_neighbors.get(node1, list()):
            if item['DST-HOST'] == node2:
                edge2 = f'{node2}:{item["SRC-IF"]}'

        result.append([edge1, edge2])

    return result
