# training-osdf-climate

## Notes

examples from Emma: https://github.com/NCAR/osdf_examples
* This looks like the simplest to implement: https://github.com/NCAR/osdf_examples/blob/main/notebooks/ndc_workflows/sonar_ai.ipynb
* these would need to be detangled from the PBS stuff:
    * https://github.com/NCAR/osdf_examples/blob/main/notebooks/geocat_climatology.ipynb
    * https://github.com/NCAR/osdf_examples/blob/main/notebooks/cesm_oceanheat.ipynb

Andrew's example: https://github.com/aowen-uwmad/osdf-python-climate

## To Dos
- get a list of potential input files we could use
- Once we decide on inputs, make a mirror somewhere in space we control
- confirm outline with everyone
- make a container?

## Outline

# Notebook 1: basic client use

## Context

We'll be using a dataset .... 
Expects the data to come from the 
[NOAA Global Historical Climatology Network](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html).

The GHCN data set is available via Amazon AWS S3, at 

```
https://noaa-ghcn-pds.s3.amazonaws.com/
```

## Access Data

To access this data in this bucket via the OSDF, we need to know the "namespace prefix" of this dataset within the OSDF.

The OSDF is already connected to AWS under the `/aws-opendata` prefix. 
The GHCN website shows the data is in the "US East 1" part of AWS, so we'll extend the OSDF namespace prefix to
`/aws-opendata/us-east-1`.
From the above link, we see that the GHCN dataset is linked in the AWS under `noaa-ghcn-pds`, so the full prefix to the
dataset in the OSDF is `/aws-opendata/us-east-1/noaa-ghcn-pds/`.

We can't (currently) list the objects in this location, but you can browse the AWS index link 
([https://noaa-ghcn-pds.s3.amazonaws.com/](https://noaa-ghcn-pds.s3.amazonaws.com/)) to see the files available.

In the top "level" of the dataset are several readme files.
Let's get the list of stations that are contained in the dataset, so we can identify what files we want to download.

The file `ghcnd-stations.txt` contains the desired list. 
This is the "object name" that we want to fetch using the OSDF.
We combine the "namespace prefix" and the "object name" together to get the desired OSDF link:
`/aws-opendata/us-east-1/noaa-ghcn-pds/ghcnd-stations.txt`.

### Fetch overall file

To download the file, we use the Pelican client with the OSDF URL:

Let's construct a Pelican URL and use it to fetch a data object: 

```
URL=blah
pelican object get $URL ./
head ./*
```

```
pelican object get osdf:///aws-opendata/us-east-1/noaa-ghcn-pds/ghcnd-stations.txt ./
```

### Identify station

There are a lot of stations listed (over 120,000!!).
Search for the one that you are interested in.

For this example, we will look at the data for the airport in Madison, WI, which shows up in the list as

```
USW00014837  43.1406  -89.3453  261.8 WI MADISON DANE CO RGNL AP                72641
```

Here, the station ID is `USW00014837`.

### Download station data

The per-station data is collected under `csv/by_station` and the filenames use the syntax `<STATION ID>.csv`. 

To download the station data, we can use the following command:

```
pelican object get osdf:///aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv
```

## Produce a visuzalization TBD

## Share data via another origin

```
URL=blah
pelican put <file> URL
```

## View other files

```
pelican ls 
```

## Can you pull one? 


- define each component of a pelican / OSDF URL (markdown text)
- list the key verbs for interacting with objects (markdown text)
- apply knowledge to get an object, create an output, and put it somewhere.
    - randomly assign a URL to each person via * magic *
    - have them get a file
    - run the script that visualizes the data
    - put the resulting file back into a common origin
    - use pelican ls
    - pull someone else's visualization + look at it. 

# Notebook 2: basic fsspec example

- same as above, but all in the notebook? 🤔
- Anything else to highlight? 

#  Notebook 3: submitting jobs

- motivation: want to do this for thousands of files
    - review the list command on the input origin
    - identify what we need to run at scale
- drill down to one job: conceptual overview - origins as where data goes/comes from as part of jobs
    - make a diagram. Excalidraw? 
- identify key config / ingredients in submit file
    - map concepts to submit file lines
    - introduce variables / queue from our list
- go through submit file together
- submit a bunch of jobs. what could go wrong. 



