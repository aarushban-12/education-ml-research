# Preliminary ASSISTments Preprocessing

This folder contains an **earlier preprocessing pipeline** that was created during the initial stages of the project.

## Why These Files Were Created

The files in this folder were created before I fully understood the preprocessing pipeline implemented by the original knowledge tracing model repository.

At the time, I was not aware that the model's own data loader already performs the necessary preprocessing of the original ASSISTments 2009 dataset. Because of this, I initially created my own preprocessing pipeline to prepare the dataset for knowledge tracing.

This resulted in two notebooks:

* `assistments_preprocessing.ipynb`
* `assistments_sakt_sequences.ipynb`

### `assistments_preprocessing.ipynb`

This notebook performs several preprocessing operations, including:

* Removing interactions with missing `skill_id` values
* Removing students with fewer than 10 interactions
* Removing skills with fewer than 100 interactions
* Rechecking student sequence lengths
* Encoding skill IDs as consecutive integers
* Saving a cleaned CSV file

The notebook produced files such as:

* `assistments_cleaned.csv`
* `assistments_sakt_ready.csv`

### `assistments_sakt_sequences.ipynb`

This notebook takes the manually cleaned dataset and converts it into student-level sequences.

It:

1. Sorts interactions chronologically using `user_id` and `order_id`
2. Groups interactions by student
3. Creates sequences containing:

   * `problem_id`
   * `skill_id`
   * `correct`
4. Splits each student's sequence temporally into:

   * 80% training
   * 10% validation
   * 10% testing
5. Saves the resulting sequences as pickle files

The notebook produced files such as:

* `train_sequences.pkl`
* `validation_sequences.pkl`
* `test_sequences.pkl`

## Why These Files Are Not Used in the Replication

After examining the original repository more carefully, I found that the model's **own data loader already performs its preprocessing**.

For example, the repository's ASSIST2009 data loader reads the original:

`skill_builder_data.csv`

and performs operations such as:

* Removing rows without a `skill_name`
* Removing duplicate `(order_id, skill_name)` pairs
* Sorting interactions by `order_id`
* Creating student-level sequences
* Mapping skills to integer indices
* Creating the `q_seqs` and `r_seqs` structures expected by the model
* Splitting sequences into the sequence lengths required by the model

Therefore, manually preprocessing the dataset beforehand would introduce an additional preprocessing pipeline that is different from the one used by the original implementation.

For the **replication portion of this project**, the appropriate procedure is to provide the original ASSISTments dataset to the repository's data loader and allow the repository to perform its intended preprocessing.

The manually generated CSV and PKL files are therefore **not inputs to the replicated model**.