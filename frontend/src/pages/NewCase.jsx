import { useState } from 'react';

export default function NewCase() {
  const [form, setForm] = useState({
    date: '',
    driver: '',
    company: '',
    truck: '',
    truck_owner: '',
    trailer: '',
    trailer_owner: '',
    location: '',
    problem: '',
    cost: '',
    payment: '',
    solution: '',
    status: '',
    culprit: '',
    efs_code: ''
  });
  const [mediaFiles, setMediaFiles] = useState([]);
  const [invoiceFile, setInvoiceFile] = useState(null);
  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };
  const handleSubmit = async e => {
    e.preventDefault();
    const data = new FormData();
    Object.entries(form).forEach(([k, v]) => data.append(k, v));
    mediaFiles.forEach(f => data.append('media_files', f));
    if (invoiceFile) data.append('invoice_file', invoiceFile);
    await fetch('http://localhost:8000/cases', {

    await fetch('/cases', {

      method: 'POST',
      body: data
    });
    alert('Case submitted');
  };
  return (
    <form onSubmit={handleSubmit} className="space-y-4 text-black">
      {Object.entries(form).map(([k, v]) => (
        <div key={k}>
          <label className="block text-white">{k}</label>
          <input
            name={k}
            value={v}
            onChange={handleChange}
            className="w-full p-1"
          />
        </div>
      ))}
      <div>
        <label className="block text-white">Media Files</label>
        <input
          type="file"
          multiple
          onChange={e => setMediaFiles([...e.target.files])}
        />
      </div>
      <div>
        <label className="block text-white">Invoice</label>
        <input
          type="file"
          onChange={e => setInvoiceFile(e.target.files[0])}
        />
      </div>
      <button type="submit" className="px-4 py-2 bg-purple-600 text-white">Submit</button>
    </form>
  );
}
