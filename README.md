# Tomato_Experiment

In order to support testing of the newer PFC design and software implementation, a test grow was performed using 3 new generation PFCs. Each of the PFC units grew a single ‘Tiny Tim’ dwarf tomato plant with each PFC supporting a different growing environment. A ‘control’ which grew the single plant utilizing 12 hours of ‘Summer Sun’ spectrum, and 12 hours of darkness. The second PFC was setup with the same lighting conditions but included 3 basil plants in the box as well. The third PFC only grew a single tomato plant, but used 12 hours of ‘Summer Sun’ with 12 hours of Blue spectrum light rather than darkness. These plants have been growing for 60 days (as of writing this report), and are continuing to grow. 

To produce actual fruit on the plants fertilization of the flowers was performed by touching the flowers with a running electric toothbrush. All three plants have produced fruit so far, with the most showing up on the ‘Blue Night’ plant, a few on the ‘Control’, and only  one or two just now showing on the plant grown with basil in the chamber. A few of the tomatoes in the ‘Blue Night’ plant have already ripened. The PFCs collected environmental data for the entire grow (with water based sensors being added in mid way through the grow). The only maintenance done on the plants has been topping off the reservoir often (almost daily as the plants got larger), and trimming the plants when they became too large for the PFCs. 

The raw data for these three PFCs have been pulled down from Google BigQuery and are in the [/raw_data/](/raw_data/) directory.
`Hidden-Snow` is the machine that ran the control environment, `Aged-Shape` had the basil plants, and `Blue-Water` was the machine that would use Blue light for the night cycle.

Inital graphing of the control data is in [/notebooks/data_process.ipynb](/notebooks/data_process.ipynb) Juypiter Notebook.
