# `Cornifer`

The [little bug](https://www.reddit.com/r/HollowKnight/comments/n646h6/iis_it_really_you_cornifer/) that could.

## Rationale

![](./assets/rationale.png)

## Usage

```console
$ git clone https://github.com/gongahkia/cornifer
$ make config
$ cd src/vision/
$ make
```

## Architecture

```mermaid
graph TD;
    V([Internet]) --> |Extracted| W[Web Scrapers]
    W --> |Scraped| Data@{shape: docs, label: "Raw Image<br>Data"}
    Data --> |Sanitised| Formatted@{ shape: tag-doc, label: "Formatted Image<br>Data"}
    Formatted --> |Stored| A@{ shape: lin-cyl, label: "Raw Image<br>corpus" }
    Formatted --> |Indexed and stored| B@{ shape: lin-cyl, label: "Labelled Image<br>corpus" }
    A --> |Preprocessing| E[OpenCV]
    E --> |Shape detection| F@{ shape: lin-cyl, label: "Processed Holds<br>corpus"}
    F --> |Sent to| G@{ shape: lin-rect, label: "Problem setting module"}
    F --> |Sent to| L@{ shape: lin-rect, label: "Problem selection module"}
    G -->|Updates| L
    M@{ shape: circle, label: "User" } -.-> |Accesses| K
    subgraph "Cornifer application"
        K[NiceGUI Frontend] --> |View all problems|L
        K --> |View sorted problems| Y
        K --> |Select holds|G
    end
    B --> |Provide training data| H@{ shape: diamond, label: "Generic ML<br>Model" }
    F --> |Provide training data| H
    H --> |Trained on data| I@{ shape: diamond, label: "Style Recognition<br>Model"}
    I --> |Runs classification| L
    L --> |Classify climbing problems based on style| Y@{ shape: lin-rect, label: "Sorted problems module"}
```

## References

The name `Cornifer` is in reference to the wandering mapmaker who aids [the Knight](https://hollowknight.fandom.com/wiki/Knight) by cartographing the kingdom of [Hallownest](https://hollowknight.fandom.com/wiki/Hallownest) from the 2017 game [Hollow Knight](https://hollowknight.fandom.com/wiki/Hollow_Knight_Wiki). [Cornifer](https://hollowknight.fandom.com/wiki/Cornifer) is often accompanied by his wife [Iselda](https://hollowknight.fandom.com/wiki/Iselda) at their shop in [Dirtmouth](https://hollowknight.fandom.com/wiki/Dirtmouth).

![](./assets/cornifer.png)

## Research

* [*Design of a sensor network for the quantitative analysis of sport climbing*](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1114539/full) by Alessandro Colombo, Ramon Maj, Marita Canina, Francesca Fedeli, Nicolo Dozio and Francesco Ferrise
* [*Indoor-Climbing-Hold-and-Route-Segmentation*](https://github.com/xiaoxiae/Indoor-Climbing-Hold-and-Route-Segmentation) Github repository by xiaoxiae

## Datasets

* [*Indoor Climbing Gym Hold And Route Segmentation*](https://www.kaggle.com/datasets/tomasslama/indoor-climbing-gym-hold-segmentation/data) Kaggle dataset by Tomáš Sláma
* [*Climbing Holds and Volumes Computer Vision Project*](https://universe.roboflow.com/blackcreed-xpgxh/climbing-holds-and-volumes) Roboflow dataset by Blackcreed
* [*Bouldering holds Computer Vision Project*](https://universe.roboflow.com/pwals/bouldering-holds-9wavr) by Pwals
* [*CLIMBNET*](https://github.com/cydivision/climbnet) Github repository by cydivision
* [*ClimbDB*](https://github.com/NehaRajganesh/ClimbDB) Github repository by NehaRajganesh
* [*bouldering_route_classification*](https://github.com/tonylay7/bouldering_route_classification) Github repository by tonylay7