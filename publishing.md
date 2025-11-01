# Panduan Publishing ke PyPI

Dokumen ini menjelaskan langkah-langkah untuk mempublish Invezgo SDK ke PyPI.

## Persiapan

1. **Install build tools**
   ```bash
   pip install build twine
   ```

2. **Update version number**
   - Edit `setup.py` dan `pyproject.toml`
   - Update `__version__` di `invezgo/__init__.py`
   - Update `CHANGELOG.md`

## Testing Local Build

1. **Build package**
   ```bash
   python -m build
   ```
   Ini akan membuat file di folder `dist/`

2. **Test install dari local**
   ```bash
   pip install dist/invezgo-sdk-1.0.0.tar.gz
   ```

## Publishing ke Test PyPI

1. **Daftar akun di Test PyPI**
   - https://test.pypi.org/account/register/

2. **Upload ke Test PyPI**
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. **Test install dari Test PyPI**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ invezgo-sdk
   ```

## Publishing ke PyPI Production

1. **Daftar akun di PyPI**
   - https://pypi.org/account/register/

2. **Upload ke PyPI**
   ```bash
   python -m twine upload dist/*
   ```

3. **Verify installation**
   ```bash
   pip install invezgo-sdk
   ```

## Tips

- Gunakan API token untuk authentication (lebih aman daripada password)
- Jangan publish versi yang sama dua kali (PyPI tidak mengizinkan)
- Pastikan semua dependencies sudah benar di `requirements.txt`
- Test thoroughly sebelum publish

## Versioning

Ikuti Semantic Versioning:
- MAJOR.MINOR.PATCH
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

## Checklist Sebelum Publish

- [ ] Semua test passed
- [ ] README.md lengkap dan benar
- [ ] Version number sudah update
- [ ] CHANGELOG.md sudah update
- [ ] License file ada
- [ ] Tidak ada hardcoded secrets
- [ ] Dependencies sudah benar

