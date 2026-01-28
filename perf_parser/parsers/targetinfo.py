import sys
import xml.etree.ElementTree as ET
from typing import List

from perf_parser.models import ClusterInfo, TargetInfo


def parse_target_info_xml(filename: str) -> List[TargetInfo]:
    tree = ET.parse(filename)
    root = tree.getroot()

    targets: List[TargetInfo] = []

    for cfg in root:
        target_info = cfg.find('TargetInfo')
        if target_info is None:
            print(f'TargetInfo missing in {cfg}')
            continue

        target = TargetInfo(
            name=target_info.attrib['Target'],
            totalNumCores=int(target_info.attrib['TotalNumCores'], 0),
            numClusters=int(target_info.attrib['NumClusters'], 0),
            clusters=[],
        )
        for cluster in cfg.findall('ClustersInfo'):
            target.clusters.append(
                ClusterInfo(
                    name=cluster.attrib['Type'],
                    id=int(cluster.attrib['Id'], 0),
                    numCores=int(cluster.attrib['NumCores'], 0),
                )
            )

        targets.append(target)

    return targets


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python targetinfo.xml')
        sys.exit()
    targets = parse_target_info_xml(sys.argv[1])

    for target in targets:
        print(target)
