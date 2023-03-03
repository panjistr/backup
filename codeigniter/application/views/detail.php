<div class="content-wrapper">
    <section class="content">
        <h4><strong>DETAIL DATA MAHASISWA</strong></h4>

        <table clas="table">
            <tr>
                <th>Nama Lengkap</th>
                <td><td><?php echo $detail->nama ?></td><t/d>
            </tr>
            <tr>
                <th>NIM</th>
                <td><td><?php echo $detail->nim ?></td><t/d>
            </tr>
            <tr>
                <th>Tanggal Lahir</th>
                <td><td><?php echo $detail->tgl_lahir ?></td><t/d>
            </tr>
            <tr>
                <th>Jurusan</th>
                <td></td><td><?php echo $detail->jurusan ?><t/d>
            </tr>
            <tr>
                <th>Alamat</th>
                <td><td><?php echo $detail->alamat ?></td><t/d>
            </tr>
            <tr>
                <th>Email</th>
                <td><td><?php echo $detail->email ?></td><t/d>
            </tr>
            <tr>
                <th>No. Telepon</th>
                <td>.<?php echo $detail->no_telp ?></td>
            </tr>
            
            <tr>
                <td>
                    <img src="<?php echo base_url(); ?>assets/foto/<?php echo $detail->foto; ?>" width="90" height="110">
                </td>    
                <td></td> 
            </tr>
        </table>

        <a href="<?php echo base_url('mahasiswa/index'); ?>" class="btn btn-primary">Kembali</a>
    </section>
</div>    