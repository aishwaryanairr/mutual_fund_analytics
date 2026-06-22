{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c20e2e2-9872-484e-a60c-340293e57886",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved sbi_smallcap_nav\n",
      "Saved sbi_bluechip\n",
      "Saved icici_bluechip\n",
      "Saved nippon_largecap\n",
      "Saved axis_bluechip\n",
      "Saved kotak_bluechip\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "os.makedirs(\"data/raw\", exist_ok=True)\n",
    "\n",
    "funds = {\n",
    "    \"sbi_smallcap_nav\": 125497,\n",
    "    \"sbi_bluechip\": 119551,\n",
    "    \"icici_bluechip\": 120503,\n",
    "    \"nippon_largecap\": 118632,\n",
    "    \"axis_bluechip\": 119092,\n",
    "    \"kotak_bluechip\": 120841\n",
    "}\n",
    "\n",
    "for fund_name, scheme_code in funds.items():\n",
    "\n",
    "    url = f\"https://api.mfapi.in/mf/{scheme_code}\"\n",
    "\n",
    "    response = requests.get(url)\n",
    "\n",
    "    if response.status_code == 200:\n",
    "\n",
    "        data = response.json()\n",
    "\n",
    "        nav_df = pd.DataFrame(data[\"data\"])\n",
    "\n",
    "        nav_df.to_csv(\n",
    "            f\"data/raw/{fund_name}.csv\",\n",
    "            index=False\n",
    "        )\n",
    "\n",
    "        print(f\"Saved {fund_name}\")\n",
    "\n",
    "    else:\n",
    "        print(f\"Failed {scheme_code}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f99f0a83-11de-4ee7-920f-bdf864c658af",
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
   "version": "3.13.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
