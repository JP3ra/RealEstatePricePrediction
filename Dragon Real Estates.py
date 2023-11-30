{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dragon Real Estate - Price Predictor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pandas\n",
      "  Downloading pandas-2.1.3-cp39-cp39-win_amd64.whl.metadata (18 kB)\n",
      "Requirement already satisfied: numpy in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (1.26.2)\n",
      "Collecting matplotlib\n",
      "  Downloading matplotlib-3.8.2-cp39-cp39-win_amd64.whl.metadata (5.9 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Collecting pytz>=2020.1 (from pandas)\n",
      "  Downloading pytz-2023.3.post1-py2.py3-none-any.whl.metadata (22 kB)\n",
      "Collecting tzdata>=2022.1 (from pandas)\n",
      "  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)\n",
      "Collecting contourpy>=1.0.1 (from matplotlib)\n",
      "  Downloading contourpy-1.2.0-cp39-cp39-win_amd64.whl.metadata (5.8 kB)\n",
      "Collecting cycler>=0.10 (from matplotlib)\n",
      "  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)\n",
      "Collecting fonttools>=4.22.0 (from matplotlib)\n",
      "  Downloading fonttools-4.45.1-cp39-cp39-win_amd64.whl.metadata (158 kB)\n",
      "     ---------------------------------------- 0.0/158.4 kB ? eta -:--:--\n",
      "     -------------------------------------- 158.4/158.4 kB 4.8 MB/s eta 0:00:00\n",
      "Collecting kiwisolver>=1.3.1 (from matplotlib)\n",
      "  Downloading kiwisolver-1.4.5-cp39-cp39-win_amd64.whl.metadata (6.5 kB)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from matplotlib) (23.2)\n",
      "Collecting pillow>=8 (from matplotlib)\n",
      "  Downloading Pillow-10.1.0-cp39-cp39-win_amd64.whl.metadata (9.6 kB)\n",
      "Collecting pyparsing>=2.3.1 (from matplotlib)\n",
      "  Downloading pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)\n",
      "Collecting importlib-resources>=3.2.0 (from matplotlib)\n",
      "  Downloading importlib_resources-6.1.1-py3-none-any.whl.metadata (4.1 kB)\n",
      "Requirement already satisfied: zipp>=3.1.0 in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from importlib-resources>=3.2.0->matplotlib) (3.17.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Downloading pandas-2.1.3-cp39-cp39-win_amd64.whl (10.8 MB)\n",
      "   ---------------------------------------- 0.0/10.8 MB ? eta -:--:--\n",
      "   -- ------------------------------------- 0.6/10.8 MB 13.5 MB/s eta 0:00:01\n",
      "   ----- ---------------------------------- 1.5/10.8 MB 15.9 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 3.1/10.8 MB 24.9 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 4.5/10.8 MB 22.0 MB/s eta 0:00:01\n",
      "   --------------------- ------------------ 5.8/10.8 MB 23.3 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 7.4/10.8 MB 24.9 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 8.8/10.8 MB 25.7 MB/s eta 0:00:01\n",
      "   -------------------------------------- - 10.4/10.8 MB 27.3 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 10.8/10.8 MB 25.2 MB/s eta 0:00:00\n",
      "Downloading matplotlib-3.8.2-cp39-cp39-win_amd64.whl (7.6 MB)\n",
      "   ---------------------------------------- 0.0/7.6 MB ? eta -:--:--\n",
      "   ----- ---------------------------------- 1.1/7.6 MB 23.7 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 2.2/7.6 MB 27.6 MB/s eta 0:00:01\n",
      "   ------------- -------------------------- 2.5/7.6 MB 17.6 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 3.1/7.6 MB 16.3 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 4.3/7.6 MB 18.3 MB/s eta 0:00:01\n",
      "   ----------------------------- ---------- 5.7/7.6 MB 20.3 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 7.1/7.6 MB 21.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 7.6/7.6 MB 20.4 MB/s eta 0:00:00\n",
      "Downloading contourpy-1.2.0-cp39-cp39-win_amd64.whl (181 kB)\n",
      "   ---------------------------------------- 0.0/181.9 kB ? eta -:--:--\n",
      "   --------------------------------------- 181.9/181.9 kB 10.7 MB/s eta 0:00:00\n",
      "Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)\n",
      "Downloading fonttools-4.45.1-cp39-cp39-win_amd64.whl (2.2 MB)\n",
      "   ---------------------------------------- 0.0/2.2 MB ? eta -:--:--\n",
      "   ------------------------ --------------- 1.3/2.2 MB 27.7 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 2.2/2.2 MB 22.9 MB/s eta 0:00:00\n",
      "Downloading importlib_resources-6.1.1-py3-none-any.whl (33 kB)\n",
      "Downloading kiwisolver-1.4.5-cp39-cp39-win_amd64.whl (56 kB)\n",
      "   ---------------------------------------- 0.0/56.2 kB ? eta -:--:--\n",
      "   ---------------------------------------- 56.2/56.2 kB ? eta 0:00:00\n",
      "Downloading Pillow-10.1.0-cp39-cp39-win_amd64.whl (2.6 MB)\n",
      "   ---------------------------------------- 0.0/2.6 MB ? eta -:--:--\n",
      "   ------------------- -------------------- 1.3/2.6 MB 27.5 MB/s eta 0:00:01\n",
      "   ---------------------------------------  2.6/2.6 MB 27.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 2.6/2.6 MB 23.8 MB/s eta 0:00:00\n",
      "Downloading pyparsing-3.1.1-py3-none-any.whl (103 kB)\n",
      "   ---------------------------------------- 0.0/103.1 kB ? eta -:--:--\n",
      "   ---------------------------------------- 103.1/103.1 kB ? eta 0:00:00\n",
      "Downloading pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)\n",
      "   ---------------------------------------- 0.0/502.5 kB ? eta -:--:--\n",
      "   --------------------------------------- 502.5/502.5 kB 30.8 MB/s eta 0:00:00\n",
      "Installing collected packages: pytz, tzdata, pyparsing, pillow, kiwisolver, importlib-resources, fonttools, cycler, contourpy, pandas, matplotlib\n",
      "Successfully installed contourpy-1.2.0 cycler-0.12.1 fonttools-4.45.1 importlib-resources-6.1.1 kiwisolver-1.4.5 matplotlib-3.8.2 pandas-2.1.3 pillow-10.1.0 pyparsing-3.1.1 pytz-2023.3.post1 tzdata-2023.3\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas numpy matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = pd.read_csv(\"data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1</td>\n",
       "      <td>296</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2</td>\n",
       "      <td>242</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "      <td>21.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.02729</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>7.185</td>\n",
       "      <td>61.1</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2</td>\n",
       "      <td>242</td>\n",
       "      <td>17.8</td>\n",
       "      <td>392.83</td>\n",
       "      <td>4.03</td>\n",
       "      <td>34.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.03237</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>6.998</td>\n",
       "      <td>45.8</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>394.63</td>\n",
       "      <td>2.94</td>\n",
       "      <td>33.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.06905</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>7.147</td>\n",
       "      <td>54.2</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3</td>\n",
       "      <td>222</td>\n",
       "      <td>18.7</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.33</td>\n",
       "      <td>36.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD  TAX  PTRATIO  \\\n",
       "0  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296     15.3   \n",
       "1  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242     17.8   \n",
       "2  0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242     17.8   \n",
       "3  0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222     18.7   \n",
       "4  0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222     18.7   \n",
       "\n",
       "        B  LSTAT  MEDV  \n",
       "0  396.90   4.98  24.0  \n",
       "1  396.90   9.14  21.6  \n",
       "2  392.83   4.03  34.7  \n",
       "3  394.63   2.94  33.4  \n",
       "4  396.90   5.33  36.2  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 506 entries, 0 to 505\n",
      "Data columns (total 14 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   CRIM     506 non-null    float64\n",
      " 1   ZN       506 non-null    float64\n",
      " 2   INDUS    506 non-null    float64\n",
      " 3   CHAS     506 non-null    int64  \n",
      " 4   NOX      506 non-null    float64\n",
      " 5   RM       501 non-null    float64\n",
      " 6   AGE      506 non-null    float64\n",
      " 7   DIS      506 non-null    float64\n",
      " 8   RAD      506 non-null    int64  \n",
      " 9   TAX      506 non-null    int64  \n",
      " 10  PTRATIO  506 non-null    float64\n",
      " 11  B        506 non-null    float64\n",
      " 12  LSTAT    506 non-null    float64\n",
      " 13  MEDV     506 non-null    float64\n",
      "dtypes: float64(11), int64(3)\n",
      "memory usage: 55.5 KB\n"
     ]
    }
   ],
   "source": [
    "housing.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CHAS\n",
       "0    471\n",
       "1     35\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>501.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.613524</td>\n",
       "      <td>11.363636</td>\n",
       "      <td>11.136779</td>\n",
       "      <td>0.069170</td>\n",
       "      <td>0.554695</td>\n",
       "      <td>6.284341</td>\n",
       "      <td>68.574901</td>\n",
       "      <td>3.795043</td>\n",
       "      <td>9.549407</td>\n",
       "      <td>408.237154</td>\n",
       "      <td>18.455534</td>\n",
       "      <td>356.674032</td>\n",
       "      <td>12.653063</td>\n",
       "      <td>22.532806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>8.601545</td>\n",
       "      <td>23.322453</td>\n",
       "      <td>6.860353</td>\n",
       "      <td>0.253994</td>\n",
       "      <td>0.115878</td>\n",
       "      <td>0.705587</td>\n",
       "      <td>28.148861</td>\n",
       "      <td>2.105710</td>\n",
       "      <td>8.707259</td>\n",
       "      <td>168.537116</td>\n",
       "      <td>2.164946</td>\n",
       "      <td>91.294864</td>\n",
       "      <td>7.141062</td>\n",
       "      <td>9.197104</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.006320</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.460000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.385000</td>\n",
       "      <td>3.561000</td>\n",
       "      <td>2.900000</td>\n",
       "      <td>1.129600</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>187.000000</td>\n",
       "      <td>12.600000</td>\n",
       "      <td>0.320000</td>\n",
       "      <td>1.730000</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.082045</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.190000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.449000</td>\n",
       "      <td>5.884000</td>\n",
       "      <td>45.025000</td>\n",
       "      <td>2.100175</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>279.000000</td>\n",
       "      <td>17.400000</td>\n",
       "      <td>375.377500</td>\n",
       "      <td>6.950000</td>\n",
       "      <td>17.025000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.256510</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.690000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.538000</td>\n",
       "      <td>6.208000</td>\n",
       "      <td>77.500000</td>\n",
       "      <td>3.207450</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>330.000000</td>\n",
       "      <td>19.050000</td>\n",
       "      <td>391.440000</td>\n",
       "      <td>11.360000</td>\n",
       "      <td>21.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.677083</td>\n",
       "      <td>12.500000</td>\n",
       "      <td>18.100000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.624000</td>\n",
       "      <td>6.625000</td>\n",
       "      <td>94.075000</td>\n",
       "      <td>5.188425</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>666.000000</td>\n",
       "      <td>20.200000</td>\n",
       "      <td>396.225000</td>\n",
       "      <td>16.955000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>88.976200</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>27.740000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.871000</td>\n",
       "      <td>8.780000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>12.126500</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>711.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>396.900000</td>\n",
       "      <td>37.970000</td>\n",
       "      <td>50.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             CRIM          ZN       INDUS        CHAS         NOX          RM  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  501.000000   \n",
       "mean     3.613524   11.363636   11.136779    0.069170    0.554695    6.284341   \n",
       "std      8.601545   23.322453    6.860353    0.253994    0.115878    0.705587   \n",
       "min      0.006320    0.000000    0.460000    0.000000    0.385000    3.561000   \n",
       "25%      0.082045    0.000000    5.190000    0.000000    0.449000    5.884000   \n",
       "50%      0.256510    0.000000    9.690000    0.000000    0.538000    6.208000   \n",
       "75%      3.677083   12.500000   18.100000    0.000000    0.624000    6.625000   \n",
       "max     88.976200  100.000000   27.740000    1.000000    0.871000    8.780000   \n",
       "\n",
       "              AGE         DIS         RAD         TAX     PTRATIO           B  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000   \n",
       "mean    68.574901    3.795043    9.549407  408.237154   18.455534  356.674032   \n",
       "std     28.148861    2.105710    8.707259  168.537116    2.164946   91.294864   \n",
       "min      2.900000    1.129600    1.000000  187.000000   12.600000    0.320000   \n",
       "25%     45.025000    2.100175    4.000000  279.000000   17.400000  375.377500   \n",
       "50%     77.500000    3.207450    5.000000  330.000000   19.050000  391.440000   \n",
       "75%     94.075000    5.188425   24.000000  666.000000   20.200000  396.225000   \n",
       "max    100.000000   12.126500   24.000000  711.000000   22.000000  396.900000   \n",
       "\n",
       "            LSTAT        MEDV  \n",
       "count  506.000000  506.000000  \n",
       "mean    12.653063   22.532806  \n",
       "std      7.141062    9.197104  \n",
       "min      1.730000    5.000000  \n",
       "25%      6.950000   17.025000  \n",
       "50%     11.360000   21.200000  \n",
       "75%     16.955000   25.000000  \n",
       "max     37.970000   50.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Train-Test Splitting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting scikit-learn\n",
      "  Downloading scikit_learn-1.3.2-cp39-cp39-win_amd64.whl.metadata (11 kB)\n",
      "Requirement already satisfied: numpy<2.0,>=1.17.3 in c:\\users\\prisha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from scikit-learn) (1.26.2)\n",
      "Collecting scipy>=1.5.0 (from scikit-learn)\n",
      "  Downloading scipy-1.11.4-cp39-cp39-win_amd64.whl.metadata (60 kB)\n",
      "     ---------------------------------------- 0.0/60.4 kB ? eta -:--:--\n",
      "     ---------------------------------------- 60.4/60.4 kB 3.1 MB/s eta 0:00:00\n",
      "Collecting joblib>=1.1.1 (from scikit-learn)\n",
      "  Downloading joblib-1.3.2-py3-none-any.whl.metadata (5.4 kB)\n",
      "Collecting threadpoolctl>=2.0.0 (from scikit-learn)\n",
      "  Downloading threadpoolctl-3.2.0-py3-none-any.whl.metadata (10.0 kB)\n",
      "Downloading scikit_learn-1.3.2-cp39-cp39-win_amd64.whl (9.3 MB)\n",
      "   ---------------------------------------- 0.0/9.3 MB ? eta -:--:--\n",
      "   - -------------------------------------- 0.2/9.3 MB 7.4 MB/s eta 0:00:02\n",
      "   --- ------------------------------------ 0.8/9.3 MB 10.5 MB/s eta 0:00:01\n",
      "   ------ --------------------------------- 1.6/9.3 MB 12.9 MB/s eta 0:00:01\n",
      "   ---------- ----------------------------- 2.5/9.3 MB 14.6 MB/s eta 0:00:01\n",
      "   -------------- ------------------------- 3.3/9.3 MB 15.1 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 3.9/9.3 MB 14.6 MB/s eta 0:00:01\n",
      "   --------------------- ------------------ 5.0/9.3 MB 15.3 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 6.1/9.3 MB 15.6 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 7.2/9.3 MB 15.8 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 8.3/9.3 MB 16.0 MB/s eta 0:00:01\n",
      "   ---------------------------------------  9.3/9.3 MB 16.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 9.3/9.3 MB 14.9 MB/s eta 0:00:00\n",
      "Downloading joblib-1.3.2-py3-none-any.whl (302 kB)\n",
      "   ---------------------------------------- 0.0/302.2 kB ? eta -:--:--\n",
      "   --------------------------------------- 302.2/302.2 kB 18.2 MB/s eta 0:00:00\n",
      "Downloading scipy-1.11.4-cp39-cp39-win_amd64.whl (44.3 MB)\n",
      "   ---------------------------------------- 0.0/44.3 MB ? eta -:--:--\n",
      "    --------------------------------------- 1.0/44.3 MB 22.0 MB/s eta 0:00:02\n",
      "   - -------------------------------------- 2.1/44.3 MB 22.1 MB/s eta 0:00:02\n",
      "   -- ------------------------------------- 2.7/44.3 MB 19.5 MB/s eta 0:00:03\n",
      "   --- ------------------------------------ 3.5/44.3 MB 17.0 MB/s eta 0:00:03\n",
      "   ---- ----------------------------------- 4.5/44.3 MB 16.8 MB/s eta 0:00:03\n",
      "   ---- ----------------------------------- 5.0/44.3 MB 15.3 MB/s eta 0:00:03\n",
      "   ----- ---------------------------------- 6.0/44.3 MB 15.9 MB/s eta 0:00:03\n",
      "   ------ --------------------------------- 6.9/44.3 MB 16.4 MB/s eta 0:00:03\n",
      "   ------- -------------------------------- 7.8/44.3 MB 16.7 MB/s eta 0:00:03\n",
      "   -------- ------------------------------- 9.3/44.3 MB 18.0 MB/s eta 0:00:02\n",
      "   --------- ------------------------------ 10.8/44.3 MB 19.2 MB/s eta 0:00:02\n",
      "   ----------- ---------------------------- 12.3/44.3 MB 20.5 MB/s eta 0:00:02\n",
      "   ------------ --------------------------- 13.5/44.3 MB 22.6 MB/s eta 0:00:02\n",
      "   ------------- -------------------------- 14.8/44.3 MB 24.2 MB/s eta 0:00:02\n",
      "   -------------- ------------------------- 16.5/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 18.0/44.3 MB 32.8 MB/s eta 0:00:01\n",
      "   ----------------- ---------------------- 19.6/44.3 MB 32.7 MB/s eta 0:00:01\n",
      "   ------------------ --------------------- 20.8/44.3 MB 29.8 MB/s eta 0:00:01\n",
      "   ------------------- -------------------- 21.7/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   -------------------- ------------------- 22.9/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 24.5/44.3 MB 28.5 MB/s eta 0:00:01\n",
      "   ----------------------- ---------------- 26.0/44.3 MB 31.2 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 27.6/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 29.3/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 30.7/44.3 MB 31.2 MB/s eta 0:00:01\n",
      "   ----------------------------- ---------- 32.1/44.3 MB 31.2 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 33.4/44.3 MB 32.7 MB/s eta 0:00:01\n",
      "   ------------------------------- -------- 34.5/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 35.9/44.3 MB 31.2 MB/s eta 0:00:01\n",
      "   ---------------------------------- ----- 37.7/44.3 MB 31.2 MB/s eta 0:00:01\n",
      "   ---------------------------------- ----- 38.5/44.3 MB 29.7 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 39.5/44.3 MB 27.3 MB/s eta 0:00:01\n",
      "   ------------------------------------ --- 40.5/44.3 MB 25.1 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 41.9/44.3 MB 26.2 MB/s eta 0:00:01\n",
      "   ---------------------------------------  43.2/44.3 MB 26.2 MB/s eta 0:00:01\n",
      "   ---------------------------------------  44.3/44.3 MB 27.3 MB/s eta 0:00:01\n",
      "   ---------------------------------------  44.3/44.3 MB 27.3 MB/s eta 0:00:01\n",
      "   ---------------------------------------  44.3/44.3 MB 27.3 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 44.3/44.3 MB 19.8 MB/s eta 0:00:00\n",
      "Downloading threadpoolctl-3.2.0-py3-none-any.whl (15 kB)\n",
      "Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn\n",
      "Successfully installed joblib-1.3.2 scikit-learn-1.3.2 scipy-1.11.4 threadpoolctl-3.2.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows in train set: 404\n",
      "Rows in test set: 102\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "train_set, test_set  = train_test_split(housing, test_size=0.2, random_state=42)\n",
    "print(f\"Rows in train set: {len(train_set)}\\nRows in test set: {len(test_set)}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Created wit the intention to have fair distribution of the categories \n",
    "from sklearn.model_selection import StratifiedShuffleSplit\n",
    "split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)\n",
    "for train_index, test_index in split.split(housing, housing['CHAS']):\n",
    "    strat_train_set = housing.loc[train_index]\n",
    "    strat_test_set = housing.loc[test_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CHAS\n",
       "0    95\n",
       "1     7\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strat_test_set['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CHAS\n",
       "0    376\n",
       "1     28\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strat_train_set['CHAS'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = strat_train_set.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Looking for Correlations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MEDV       1.000000\n",
       "RM         0.680857\n",
       "B          0.361761\n",
       "ZN         0.339741\n",
       "DIS        0.240451\n",
       "CHAS       0.205066\n",
       "AGE       -0.364596\n",
       "RAD       -0.374693\n",
       "CRIM      -0.393715\n",
       "NOX       -0.422873\n",
       "TAX       -0.456657\n",
       "INDUS     -0.473516\n",
       "PTRATIO   -0.493534\n",
       "LSTAT     -0.740494\n",
       "Name: MEDV, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_matrix = housing.corr()\n",
    "corr_matrix['MEDV'].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Trying out Attribute combinations\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "housing[\"TAXRM\"] = housing['TAX']/housing['RM']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>MEDV</th>\n",
       "      <th>TAXRM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>254</th>\n",
       "      <td>0.04819</td>\n",
       "      <td>80.0</td>\n",
       "      <td>3.64</td>\n",
       "      <td>0</td>\n",
       "      <td>0.392</td>\n",
       "      <td>6.108</td>\n",
       "      <td>32.0</td>\n",
       "      <td>9.2203</td>\n",
       "      <td>1</td>\n",
       "      <td>315</td>\n",
       "      <td>16.4</td>\n",
       "      <td>392.89</td>\n",
       "      <td>6.57</td>\n",
       "      <td>21.9</td>\n",
       "      <td>51.571709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>348</th>\n",
       "      <td>0.01501</td>\n",
       "      <td>80.0</td>\n",
       "      <td>2.01</td>\n",
       "      <td>0</td>\n",
       "      <td>0.435</td>\n",
       "      <td>6.635</td>\n",
       "      <td>29.7</td>\n",
       "      <td>8.3440</td>\n",
       "      <td>4</td>\n",
       "      <td>280</td>\n",
       "      <td>17.0</td>\n",
       "      <td>390.94</td>\n",
       "      <td>5.99</td>\n",
       "      <td>24.5</td>\n",
       "      <td>42.200452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>476</th>\n",
       "      <td>4.87141</td>\n",
       "      <td>0.0</td>\n",
       "      <td>18.10</td>\n",
       "      <td>0</td>\n",
       "      <td>0.614</td>\n",
       "      <td>6.484</td>\n",
       "      <td>93.6</td>\n",
       "      <td>2.3053</td>\n",
       "      <td>24</td>\n",
       "      <td>666</td>\n",
       "      <td>20.2</td>\n",
       "      <td>396.21</td>\n",
       "      <td>18.68</td>\n",
       "      <td>16.7</td>\n",
       "      <td>102.714374</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>321</th>\n",
       "      <td>0.18159</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.38</td>\n",
       "      <td>0</td>\n",
       "      <td>0.493</td>\n",
       "      <td>6.376</td>\n",
       "      <td>54.3</td>\n",
       "      <td>4.5404</td>\n",
       "      <td>5</td>\n",
       "      <td>287</td>\n",
       "      <td>19.6</td>\n",
       "      <td>396.90</td>\n",
       "      <td>6.87</td>\n",
       "      <td>23.1</td>\n",
       "      <td>45.012547</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>326</th>\n",
       "      <td>0.30347</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.38</td>\n",
       "      <td>0</td>\n",
       "      <td>0.493</td>\n",
       "      <td>6.312</td>\n",
       "      <td>28.9</td>\n",
       "      <td>5.4159</td>\n",
       "      <td>5</td>\n",
       "      <td>287</td>\n",
       "      <td>19.6</td>\n",
       "      <td>396.90</td>\n",
       "      <td>6.15</td>\n",
       "      <td>23.0</td>\n",
       "      <td>45.468948</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD  TAX  \\\n",
       "254  0.04819  80.0   3.64     0  0.392  6.108  32.0  9.2203    1  315   \n",
       "348  0.01501  80.0   2.01     0  0.435  6.635  29.7  8.3440    4  280   \n",
       "476  4.87141   0.0  18.10     0  0.614  6.484  93.6  2.3053   24  666   \n",
       "321  0.18159   0.0   7.38     0  0.493  6.376  54.3  4.5404    5  287   \n",
       "326  0.30347   0.0   7.38     0  0.493  6.312  28.9  5.4159    5  287   \n",
       "\n",
       "     PTRATIO       B  LSTAT  MEDV       TAXRM  \n",
       "254     16.4  392.89   6.57  21.9   51.571709  \n",
       "348     17.0  390.94   5.99  24.5   42.200452  \n",
       "476     20.2  396.21  18.68  16.7  102.714374  \n",
       "321     19.6  396.90   6.87  23.1   45.012547  \n",
       "326     19.6  396.90   6.15  23.0   45.468948  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MEDV       1.000000\n",
       "RM         0.680857\n",
       "B          0.361761\n",
       "ZN         0.339741\n",
       "DIS        0.240451\n",
       "CHAS       0.205066\n",
       "AGE       -0.364596\n",
       "RAD       -0.374693\n",
       "CRIM      -0.393715\n",
       "NOX       -0.422873\n",
       "TAX       -0.456657\n",
       "INDUS     -0.473516\n",
       "PTRATIO   -0.493534\n",
       "TAXRM     -0.528626\n",
       "LSTAT     -0.740494\n",
       "Name: MEDV, dtype: float64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_matrix = housing.corr()\n",
    "corr_matrix['MEDV'].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "housing = strat_train_set.drop(\"MEDV\", axis=1)\n",
    "housing_labels = strat_train_set[\"MEDV\"].copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Creating a Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.impute import SimpleImputer\n",
    "my_pipeline = Pipeline([\n",
    "    ('imputer', SimpleImputer(strategy=\"median\")),\n",
    "    #     ..... add as many as you want in your pipeline\n",
    "    ('std_scaler', StandardScaler()),\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "housing_num_tr = my_pipeline.fit_transform(housing)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(404, 13)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "housing_num_tr.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Selecting a desired model for Dragon Real Estates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestRegressor()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestRegressor</label><div class=\"sk-toggleable__content\"><pre>RandomForestRegressor()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestRegressor()"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "# model = LinearRegression()\n",
    "# model = DecisionTreeRegressor()\n",
    "model = RandomForestRegressor()\n",
    "model.fit(housing_num_tr, housing_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "some_data = housing.iloc[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "some_labels = housing_labels.iloc[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "prepared_data = my_pipeline.transform(some_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([22.152, 25.663, 16.251, 23.494, 23.625])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(prepared_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[21.9, 24.5, 16.7, 23.1, 23.0]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(some_labels)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluating the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "housing_predictions = model.predict(housing_num_tr)\n",
    "mse = mean_squared_error(housing_labels, housing_predictions)\n",
    "rmse = np.sqrt(mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.274726722800531"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rmse"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Saving the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Dragon.joblib']"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump, load\n",
    "dump(model, 'Dragon.joblib') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Testing the model on test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test = strat_test_set.drop(\"MEDV\", axis=1)\n",
    "Y_test = strat_test_set[\"MEDV\"].copy()\n",
    "X_test_prepared = my_pipeline.transform(X_test)\n",
    "final_predictions = model.predict(X_test_prepared)\n",
    "final_mse = mean_squared_error(Y_test, final_predictions)\n",
    "final_rmse = np.sqrt(final_mse)\n",
    "# print(final_predictions, list(Y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.2156768262654114"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_rmse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,\n",
       "       -0.23979304, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,\n",
       "       -0.97491834,  0.41164221, -0.86091034])"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prepared_data[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Using the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([23.02])"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump, load\n",
    "import numpy as np\n",
    "model = load('Dragon.joblib') \n",
    "features = np.array([[-5.43942006, 4.12628155, -1.6165014, -0.67288841, -1.42262747,\n",
    "       -11.44443979304, -49.31238772,  7.61111401, -26.0016879 , -0.5778192 ,\n",
    "       -0.97491834,  0.41164221, -66.86091034]])\n",
    "model.predict(features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
